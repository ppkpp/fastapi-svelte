
from fastapi import APIRouter, Depends,Request
import asyncio
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