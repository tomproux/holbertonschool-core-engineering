#!/usr/bin/env python3
"""Simple WebSocket client for the echo server."""

import asyncio
import os
import sys

import websockets


async def connect_and_send(uri=None, message=None):
    """Connect to a WebSocket server, send a message, and return the echo."""
    if uri is None:
        uri = os.getenv("WS_URI", "ws://localhost:8765")

    if message is None:
        if len(sys.argv) > 1:
            message = sys.argv[1]
        else:
            message = os.getenv("WS_MESSAGE", "demo")

    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()

    return response


if __name__ == "__main__":
    response = asyncio.run(connect_and_send())
    sys.stdout.write(response)
