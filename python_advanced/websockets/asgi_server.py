#!/usr/bin/env python3
"""Minimal ASGI server for the WebSocket chat client."""

from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

BASE_DIR = Path(__file__).resolve().parent
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
