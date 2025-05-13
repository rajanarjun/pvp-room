#!/usr/bin/env python
import asyncio
from websockets.asyncio.client import connect

async def hello():
    async with connect("ws://localhost:6969") as websocket:
        await websocket.send("Hello world!")
        msg = await websocket.recv()
        print(msg)

if __name__ == "__main__":
    asyncio.run(hello())
