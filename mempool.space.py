#!/usr/bin/env python3
import websocket
import _thread
import time
import rel
import json

rel.safe_read()


def on_message(ws, message):
    print(json.loads(message))


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    message = {"action": "init"}
    ws.send(json.dumps(message))
    message = {"action": "want",
               "data": [
                   'blocks',
                   'stats',
                   'mempool-blocks',
                   'live-2h-chart',
                   'watch-mempool']
               }
    ws.send(json.dumps(message))


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://mempool.space/api/v1/ws",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
