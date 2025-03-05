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
day_volume = 0
opening_price = 0
susp_opening_price = 0
high_price = 0
low_price = 0
susp_high_price = 0
susp_low_price = 0

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
    global day_volume, opening_price, susp_opening_price, high_price, low_price, susp_high_price, susp_low_price
    
    if "volume" in data:
        day_volume = data["volume"]
        debug_log("Aktualisierung der Tagesdaten:")
        debug_log(f"📈 Volumen: {day_volume}")

    if "open" in data:
        opening_price = data["open"]
        debug_log("Aktualisierung der Tagesdaten:")
        debug_log(f"📈 Eröffnungskurs: {opening_price}")

    if "suspOpen" in data:
        susp_opening_price = data["suspOpen"]
        debug_log("Aktualisierung der Tagesdaten:")
        debug_log(f"📈 Suspended Eröffnungskurs: {susp_opening_price}")

    if "high" in data:
        high_price = data["high"]
        debug_log("Aktualisierung der Tagesdaten:")
        debug_log(f"📈 Höchstkurs: {high_price}")
    
    if "low" in data:
        low_price = data["low"]
        debug_log("Aktualisierung der Tagesdaten:")
        debug_log(f"📈 Tiefstkurs: {low_price}")
    
    if "suspHigh" in data:
        susp_high_price = data["suspHigh"]
        debug_log("Aktualisierung der Tagesdaten:")
        debug_log(f"📈 Suspended Höchstkurs: {susp_high_price}")
    
    if "suspLow" in data:
        susp_low_price = data["suspLow"]
        debug_log("Aktualisierung der Tagesdaten:")
        debug_log(f"📈 Suspended Tiefstkurs: {susp_low_price}")
    
    if "last" in data and "tradeVolume" in data and "tradeTime" in data:
        trade_time = data["tradeTime"]
        last_price = data["last"]
        trade_volume = data["tradeVolume"]
        trades.append((trade_time, last_price, trade_volume))

        debug_log(f"📈 Neuer Trade: Zeit={trade_time}, Preis={last_price}, Volumen={trade_volume}")
    else:
        debug_log("Ungültige Live-Daten erhalten:")
        debug_log(data)
        
def get_market_data():
    return {
        "day_volume": day_volume,
        "opening_price": opening_price,
        "susp_opening_price": susp_opening_price,
        "high_price": high_price,
        "low_price": low_price,
        "susp_high_price": susp_high_price,
        "susp_low_price": susp_low_price
    }
