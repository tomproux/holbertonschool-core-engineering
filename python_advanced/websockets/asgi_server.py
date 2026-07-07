#!/usr/bin/env python3
"""Minimal ASGI server for the WebSocket chat client."""

from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket, WebSocketDisconnect

BASE_DIR = Path(__file__).resolve().parent


async def homepage(request):
    """Serve the chat page."""
    html = (BASE_DIR / "index.html").read_text(encoding="utf-8")
    return HTMLResponse(html)


async def websocket_endpoint(websocket: WebSocket):
    """Echo incoming messages back to the sender."""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)

app = FastAPI()


@app.get("/")
async def get_index():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/styles.css")
async def get_styles():
    return FileResponse(BASE_DIR / "styles.css")


@app.get("/chat.js")
async def get_chat_script():
    return FileResponse(BASE_DIR / "chat.js")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass
