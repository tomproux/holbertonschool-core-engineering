#!/usr/bin/env python3
"""Simple WebSocket validation server."""

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Validate incoming text messages and respond with a validation status."""
    try:
        async for message in websocket:
            if isinstance(message, str):
                trimmed_message = message.strip()
                if trimmed_message:
                    await websocket.send("OK:{}".format(trimmed_message))
                else:
                    await websocket.send("invalid")
            else:
                await websocket.send("invalid")
    except ConnectionClosed:
        pass


async def main():
    """Start the validation server on localhost:8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
