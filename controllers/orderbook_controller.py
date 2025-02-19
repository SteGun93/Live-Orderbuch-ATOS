import os
from dotenv import load_dotenv
from collections import defaultdict, deque

load_dotenv()
DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "yes")

def debug_log(message):
    if DEBUG:
        print(message)

orderbook_bids = defaultdict(lambda: {"price": None, "quantity": None, "size": None})
orderbook_asks = defaultdict(lambda: {"price": None, "quantity": None, "size": None})
trades = deque(maxlen=50)

def handle_orderbook(data):
    book_row = data.get("bookRow", None)
    if book_row is None:
        return

    if "bidPrice" in data or "bidQuantity" in data or "bidSize" in data:
        if "bidPrice" in data:
            orderbook_bids[book_row]["price"] = data["bidPrice"]
        if "bidQuantity" in data:
            orderbook_bids[book_row]["quantity"] = data["bidQuantity"]
        if "bidSize" in data:
            orderbook_bids[book_row]["size"] = data["bidSize"]

    if "askPrice" in data or "askQuantity" in data or "askSize" in data:
        if "askPrice" in data:
            orderbook_asks[book_row]["price"] = data["askPrice"]
        if "askQuantity" in data:
            orderbook_asks[book_row]["quantity"] = data["askQuantity"]
        if "askSize" in data:
            orderbook_asks[book_row]["size"] = data["askSize"]

    if all(value is None for value in orderbook_bids[book_row].values()):
        orderbook_bids.pop(book_row, None)
    if all(value is None for value in orderbook_asks[book_row].values()):
        orderbook_asks.pop(book_row, None)

    debug_log(f"📊 Orderbuch aktualisiert: Bids: {orderbook_bids}, Asks: {orderbook_asks}")

def handle_trades(data):
    if "last" in data and "tradeVolume" in data and "tradeTime" in data:
        trade_time = data["tradeTime"]
        last_price = data["last"]
        trade_volume = data["tradeVolume"]
        trades.append((trade_time, last_price, trade_volume))

        debug_log(f"📈 Neuer Trade: Zeit={trade_time}, Preis={last_price}, Volumen={trade_volume}")
    else:
        debug_log("⚠ Keine gültigen Trade-Daten oder theoretischer Preis empfangen, ignoriert.")
