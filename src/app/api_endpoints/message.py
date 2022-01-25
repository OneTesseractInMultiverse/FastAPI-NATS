from fastapi import APIRouter
from app.schemas.message import Message
from app.messaging.nats_messaging_client import NATSMessagingClient
from app.logging.syslog_impl import SimpleLogger
router = APIRouter()


# -----------------------------------------------------------------------------
# POST MESSAGE
# -----------------------------------------------------------------------------
@router.post('/message', tags=['v1', 'Message'])
async def broadcast_message(message: Message):
    messaging = NATSMessagingClient(
        logger=SimpleLogger()  # Inject logger through dependency inversion
    )
    await messaging.broadcast_message(
        message=message.body,
        subject=message.subject
    )
    return message.body


# -----------------------------------------------------------------------------
# POST MESSAGE
# -----------------------------------------------------------------------------
@router.post('/message-response', tags=['v1', 'Message'])
async def request_message_with_response(message: Message):
    messaging = NATSMessagingClient(
        logger=SimpleLogger()  # Inject logger through dependency inversion
    )
    response = await messaging.submit_message_with_response(
        message=message.body,
        subject=message.subject
    )
    return response
