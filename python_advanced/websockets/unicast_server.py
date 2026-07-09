#!/usr/bin/env python3
"""Simple WebSocket unicast server."""

import asyncio

import websockets


connected_clients = set()


async def connection_handler(websocket):
    """Track each client and send replies only to the sender."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket server on localhost:8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
