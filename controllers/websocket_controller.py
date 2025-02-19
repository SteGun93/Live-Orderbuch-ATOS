import asyncio
import websockets
import json
import os
from dotenv import load_dotenv
from services.login_service import get_boursorama_login
from controllers.orderbook_controller import handle_orderbook, handle_trades

load_dotenv()
DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "yes")
TICKER = os.getenv("TICKER", "1rPATO")
EXCHANGE = os.getenv("EXCHANGE", "PAR")

def debug_log(message):
    if DEBUG:
        print(message)

async def connect_websocket():
    while True:
        debug_log("🔄 Starte neuen Login-Versuch...")
        login, password = get_boursorama_login()
        
        if not login or not password:
            debug_log("⚠ Login fehlgeschlagen, versuche erneut in 10 Sekunden...")
            await asyncio.sleep(10)
            continue

        debug_log(f"🔑 Login-Daten erhalten: {login} / {password}")

        try:
            debug_log("🌐 Versuche WebSocket-Verbindung herzustellen...")
            async with websockets.connect(
                "wss://streaming.boursorama.com/quotes",
                ping_interval=None,
                close_timeout=10
            ) as ws:
                debug_log("✅ WebSocket-Verbindung hergestellt!")

                debug_log("📡 Sende Orderbuch-Subscription...")
                await ws.send(json.dumps({
                    "channel": "feed.streaming.join",
                    "user": {"login": login, "password": password},
                    "data": {
                        "connection": {"login": login, "password": password},
                        "feed": f"#book{EXCHANGE}-{TICKER}"
                    }
                }))

                debug_log("📡 Sende Ticker-Subscription...")
                await ws.send(json.dumps({
                    "channel": "feed.streaming.join",
                    "user": {"login": login, "password": password},
                    "data": {
                        "connection": {"login": login, "password": password},
                        "feed": f"#live{EXCHANGE}-{TICKER}"
                    }
                }))

                debug_log("✅ Subscriptions erfolgreich gesendet! Warte auf Daten...")

                while True:
                    debug_log("⏳ Warte auf Nachricht vom WebSocket...")
                    message = await ws.recv()
                    debug_log("📥 Nachricht empfangen!")

                    data = json.loads(message)
                    debug_log(f"📩 Rohdaten: {json.dumps(data, indent=2)}")

                    if "channel" in data and data["channel"] == "feed.streaming.access_denied":
                        debug_log("❌ Zugang verweigert – hole neue Login-Daten...")
                        break 

                    if "channel" in data and data["channel"] == "feed.streaming.log":
                        debug_log(f"ℹ WebSocket-Log: {data['data']['message']}")
                        continue 

                    if "data" in data and "symbol" in data["data"]:
                        data_type = data["data"]["type"]
                        payload = data["data"]["data"]

                        if data_type == "book":
                            handle_orderbook(payload)
                        elif data_type == "live":
                            handle_trades(payload)
        except Exception as e:
            debug_log(f"⚠ WebSocket-Fehler: {e}, erneuter Versuch in 10 Sekunden...")
            await asyncio.sleep(10)
