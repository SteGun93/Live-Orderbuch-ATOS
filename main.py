import asyncio
from flask import Flask, render_template, jsonify
from controllers.websocket_controller import connect_websocket
from controllers.orderbook_controller import orderbook_bids, orderbook_asks, trades

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify({
        "bids": orderbook_bids,
        "asks": orderbook_asks,
        "trades": list(trades)
    })

websocket_started = False

if __name__ == '__main__':
    if not websocket_started:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_in_executor(None, asyncio.run, connect_websocket())
        websocket_started = True

    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
