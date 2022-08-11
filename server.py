import asyncio
import websockets
import json
import re
from datetime import datetime

#empty set
connected = set()

async def server(websocket, path):

    connected.add(websocket)
    try:
        async for message in websocket:
                for conn in connected:
                    cleanr = re.compile('<.*?>')
                    message = re.sub(cleanr, '', message)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    await conn.send(f'({current_time}) {message}')
                    
    finally:

        connected.remove(websocket)
    

start_server = websockets.serve(server, "10.174.76.150", 5000)

print("server is running...")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
