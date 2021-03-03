import asyncio
import json
from app.settings import NATS_SERVER
from nats.aio.client import Client as NATSClient
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers


class NATSMessagingClient:

    # -------------------------------------------------------------------------
    # CLASS CONSTRUCTOR
    # -------------------------------------------------------------------------
    def __init__(self):
        self._nats_client = NATSClient()

    def _connect(self):
        self._nats_client.connect()
