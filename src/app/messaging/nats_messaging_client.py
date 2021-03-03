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
        self._connected = self._connect()

    # -------------------------------------------------------------------------
    # PROPERTY CONNECTED
    # -------------------------------------------------------------------------
    @property
    def connected(self) -> bool:
        """
        If there is an active connection with NATS server this will return True
        :return:
        """
        return self._connected

    # -----------------------------------------------------------------------------
    # BROADCAST WITH LOOP
    # -----------------------------------------------------------------------------
    async def __broadcast_with_loop(self, message: dict, subject: str):
        try:
            self._connected = self._connect()
            await self._nats_client.publish(
                subject,
                json.dumps(message).encode()
            )
            await self._nats_client.close()
            self._connected = False
        except ErrTimeout as et:
            print(et)
            # TODO link to proper logging
        except ErrConnectionClosed as ecc:
            print(ecc)
            # TODO link to proper logging
        except Exception as ex:
            print(ex)
            # TODO link to proper logging

    # -------------------------------------------------------------------------
    # METHOD CONNECT
    # -------------------------------------------------------------------------
    def _connect(self):
        try:
            self._nats_client.connect(
                servers=[NATS_SERVER]
            )
            return True
        except ErrNoServers as ens:
            #  TODO link logging
            print(ens)
        except Exception as e:
            #  TODO link logging
            print(e)
        finally:
            return False


