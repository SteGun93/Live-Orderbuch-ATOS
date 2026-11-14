import asyncio
import json
import os
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

os.environ["DEBUG"] = "false"
os.environ["PYTHON_DOTENV_DISABLED"] = "1"

from controllers import orderbook_controller as book
from controllers import websocket_controller as stream
from services import login_service
from main import app


class NoNetwork:
    def setUp(self):
        super().setUp()
        self.enterContext(patch("socket.socket.connect", side_effect=AssertionError("No network in tests")))
        self.enterContext(patch("requests.sessions.Session.request", side_effect=AssertionError("HTTP must be mocked")))


class OrderbookTests(NoNetwork, unittest.TestCase):
    def setUp(self):
        super().setUp()
        book.orderbook_bids.clear()
        book.orderbook_asks.clear()
        book.trades.clear()
        for name in ("day_volume", "opening_price", "susp_opening_price",
                     "high_price", "low_price", "susp_high_price", "susp_low_price"):
            setattr(book, name, 0)

    def test_partial_update_preserves_other_values_and_is_repeatable(self):
        book.handle_orderbook({"bookRow": 1, "bidPrice": 10.25, "bidQuantity": 7, "askPrice": 10.5})
        book.handle_orderbook({"bookRow": 1, "bidPrice": 10.3})
        book.handle_orderbook({"bookRow": 1, "bidPrice": 10.3})
        self.assertEqual(book.orderbook_bids[1], {"price": 10.3, "quantity": 7, "size": None})
        self.assertEqual(book.orderbook_asks[1]["price"], 10.5)
        self.assertEqual(len(book.orderbook_bids), 1)

    def test_empty_and_missing_row_do_not_invent_quotes(self):
        book.handle_orderbook({})
        book.handle_orderbook({"bookRow": 1})
        self.assertFalse(book.orderbook_bids)
        self.assertFalse(book.orderbook_asks)

    def test_incomplete_trade_is_not_added(self):
        book.handle_trades({"last": 10})
        self.assertFalse(book.trades)

    def test_trades_keep_arrival_order_and_are_bounded(self):
        for value in range(51):
            book.handle_trades({"last": value, "tradeVolume": 2, "tradeTime": f"fixture-{50-value}"})
        self.assertEqual(len(book.trades), 50)
        self.assertEqual(book.trades[0], ("fixture-49", 1, 2))
        self.assertEqual(book.trades[-1], ("fixture-0", 50, 2))

    def test_data_route_returns_quotes_trades_and_market_totals(self):
        book.handle_orderbook({"bookRow": 1, "bidPrice": 10, "askPrice": 11})
        book.handle_trades({"volume": 123, "open": 9, "last": 10, "tradeVolume": 4, "tradeTime": "fixture-time"})
        response = app.test_client().get("/data")
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["bids"]["1"]["price"], 10)
        self.assertEqual(payload["day_volume"], 123)
        self.assertEqual(payload["trades"], [["fixture-time", 10, 4]])

    def test_index_renders_without_starting_websocket(self):
        with patch.object(stream, "connect_websocket", side_effect=AssertionError("Unexpected connection")):
            response = app.test_client().get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Orderbuch", response.data)


class LoginTests(NoNetwork, unittest.TestCase):
    def response(self, config):
        response = MagicMock()
        response.json.return_value = {"config": config}
        return response

    def test_login_uses_timeout_and_returns_fixture_credentials(self):
        response = self.response({"login": "fixture-user", "password": "fixture-password"})
        with patch.object(login_service.requests, "get", return_value=response) as request:
            self.assertEqual(login_service.get_boursorama_login(), ("fixture-user", "fixture-password"))
        self.assertEqual(request.call_args.kwargs["timeout"], 10)

    def test_placeholder_credentials_are_retried_without_waiting(self):
        responses = [self.response({"login": "login", "password": "password"}),
                     self.response({"login": "fixture-user", "password": "fixture-password"})]
        with patch.object(login_service.requests, "get", side_effect=responses) as request, \
             patch.object(login_service.time, "sleep") as sleep:
            self.assertEqual(login_service.get_boursorama_login(), ("fixture-user", "fixture-password"))
        self.assertEqual(request.call_count, 2)
        sleep.assert_called_once_with(10)

    def test_http_failure_returns_no_credentials(self):
        with patch.object(login_service.requests, "get", side_effect=login_service.requests.RequestException("fixture")):
            self.assertEqual(login_service.get_boursorama_login(), (None, None))


class StreamTests(NoNetwork, unittest.IsolatedAsyncioTestCase):
    async def test_login_failure_has_a_ten_second_retry_delay(self):
        with patch.object(stream, "get_boursorama_login", return_value=(None, None)), \
             patch.object(stream.asyncio, "sleep", new=AsyncMock(side_effect=asyncio.CancelledError)) as sleep, \
             patch.object(stream.websockets, "connect") as connect:
            with self.assertRaises(asyncio.CancelledError):
                await stream.connect_websocket()
        sleep.assert_awaited_once_with(10)
        connect.assert_not_called()

    async def test_subscriptions_dispatch_messages_and_reauthenticate_after_access_denied(self):
        messages = [
            {"data": {"symbol": "fixture", "type": "book", "data": {"bookRow": 1, "bidPrice": 10}}},
            {"data": {"symbol": "fixture", "type": "live", "data": {"volume": 20}}},
            {"channel": "feed.streaming.access_denied"},
        ]
        socket = MagicMock()
        socket.send = AsyncMock()
        socket.recv = AsyncMock(side_effect=[json.dumps(message) for message in messages])
        context = MagicMock()
        context.__aenter__ = AsyncMock(return_value=socket)
        context.__aexit__ = AsyncMock(return_value=False)
        with patch.object(stream, "get_boursorama_login", side_effect=[
                ("fixture-user", "fixture-password"), asyncio.CancelledError]), \
             patch.object(stream.websockets, "connect", return_value=context), \
             patch.object(stream, "handle_orderbook") as quotes, \
             patch.object(stream, "handle_trades") as trades:
            with self.assertRaises(asyncio.CancelledError):
                await stream.connect_websocket()
        self.assertEqual(socket.send.await_count, 2)
        subscription = json.loads(socket.send.await_args_list[0].args[0])
        self.assertEqual(subscription["channel"], "feed.streaming.join")
        quotes.assert_called_once_with({"bookRow": 1, "bidPrice": 10})
        trades.assert_called_once_with({"volume": 20})
