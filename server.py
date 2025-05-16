#!/usr/bin/env python3
import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    print(f"Received: {data.decode()}")
    writer.write(b"Hello from Python server!")
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 12345)
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())

