import asyncio
import time
import websockets
import datetime
import multiprocessing as mp


if __name__ == "__main__":
    async def handler(websocket, path):
        while True:
            now = datetime.datetime.utcnow().isoformat() + "Z"
            await websocket.send(f"From Mock TCP Server: {now}")
            time.sleep(0.1)

    start_server = websockets.serve(handler, host="10.241.238.4", port=30105)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()