#!/usr/bin/env python3
"""ASGI application using Starlette for HTTP and WebSocket echo."""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket, WebSocketDisconnect


async def homepage(request):
    """Serve a simple HTML page for the browser client."""
    html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>WebSocket App</title>
</head>
<body>
    <h1>WebSocket App</h1>
    <p>The server is running.</p>
</body>
</html>"""
    return HTMLResponse(html)


async def websocket_endpoint(websocket: WebSocket):
    """Accept WebSocket connections and echo incoming messages."""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
