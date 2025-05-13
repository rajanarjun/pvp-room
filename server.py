#!/usr/bin/env python3
import asyncio
import websockets

IP_ADDR = "0.0.0.0"
PORT_NO = 6969

async def handler(websocket):
    client_address = websocket.remote_address
    print(f"Client connected: {client_address}")
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send("received greetings")

async def run_server(ip_addr, port_no):
    async with websockets.serve(handler, ip_addr, port_no):
        print(f"Server running at ws://{ip_addr}:{port_no}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(run_server(IP_ADDR, PORT_NO))
