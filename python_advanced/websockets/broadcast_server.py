#!/usr/bin/env python3
"""Simple WebSocket broadcast server."""

import asyncio

import websockets


connected_clients = list()


async def connection_handler(websocket):
    """Track each client and broadcast incoming messages to all clients."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            broadcast_message = f"B:{message}"
            for client in list(connected_clients):
                await client.send(broadcast_message)
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket server on localhost:8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
