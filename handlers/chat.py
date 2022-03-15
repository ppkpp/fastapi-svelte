
from fastapi import APIRouter, Depends,Request, WebSocket, WebSocketDisconnect
import asyncio
from typing import List
from fastapi.responses import HTMLResponse
from sse_starlette.sse import EventSourceResponse
from configs.setting import Settings


settings = Settings()
router = APIRouter()

@router.get('/stream')
async def message_stream(request: Request):
    def new_messages():
        # Add logic here to check for new messages
        yield 'New Message'

    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            # Checks for new messages and return them to client if any
            if new_messages():
                yield {
                        "event": "new_message",
                        "id": "message_id",
                        "retry": settings.MESSAGE_STREAM_RETRY_TIMEOUT,
                        "data": "message_content"
                }

            await asyncio.sleep(settings.MESSAGE_STREAM_DELAY)

    return EventSourceResponse(event_generator())




html = """<!DOCTYPE html><html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws_id"></span></h2>
		#Added the room_id parameter
		<h2>Room ID: <span id="room_id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now ()
            document.getElementById("ws_id").textContent = client_id;
			
			var room_id = "room" + Math.floor(Math.random() * 10) % 3;
			document.getElementById("room_id").textContent = room_id;		 

			var ws = new WebSocket(`ws://localhost:8000/ws/${room_id}/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body></html>"""
    
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict = {}
    
    async def connect(self, room_id:str, websocket: WebSocket):
        await websocket.accept()
        if room_id in self.active_connections:
            self.active_connections[room_id].append(websocket)
        else:
            self.active_connections[room_id] = []	
            self.active_connections[room_id].append(websocket)
    def disconnect(self, room_id:str, websocket: WebSocket):
        self.active_connections[room_id].remove(websocket)
        
    async def send_personal_message(self, message: str, room_id:str, websocket: WebSocket):
        await websocket.send_text(message)
        
    async def broadcast(self, message: str, room_id:str):
        for connection in self.active_connections[room_id]:
            await connection.send_text(message)


manager = ConnectionManager()
@router.get("/chatui")
async def get():
        return HTMLResponse(html)
        
@router.websocket("/ws/{room_id}/{client_id}")
async def websocket_endpoint(websocket: WebSocket, room_id:str, client_id: int):
    await manager.connect(room_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", room_id, websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}", room_id)
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", room_id)