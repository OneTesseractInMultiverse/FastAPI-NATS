from app.logging import MicroserviceLogger, LogLevel
import logging
import datetime


# -----------------------------------------------------------------------------
# CLASS LOG EVENT
# -----------------------------------------------------------------------------
class LogEvent(object):

    # -------------------------------------------------------------------------
    # CONSTRUCTOR
    # -------------------------------------------------------------------------
    def __init__(self, message, level: LogLevel):
        self._message: str = message
        self._level: LogLevel = level
        self._utc_datetime = datetime.datetime.utcnow()

    # -------------------------------------------------------------------------
    # METHOD UTC TIMESTAMP
    # -------------------------------------------------------------------------
    @property
    def utc_timestamp(self) -> datetime.datetime:
        return self._utc_datetime

    # -------------------------------------------------------------------------
    # METHOD DICT
    # -------------------------------------------------------------------------
    def dict(self) -> dict:
        return {
            'message': self._message,
            'level': self._level.name,
            'utc_datetime': self._utc_datetime
        }

    # -------------------------------------------------------------------------
    # METHOD STR
    # -------------------------------------------------------------------------
    def __str__(self) -> str:
        return "[{level}: {utc_datetime}]: {message}".format(
            level=self._level.name,
            utc_datetime=str(self._utc_datetime),
            message=self._message
        )


# -----------------------------------------------------------------------------
# CLASS SIMPLE LOGGER
# -----------------------------------------------------------------------------
class SimpleAppSecLogger(MicroserviceLogger):

    def debug(self, message: str, **kwargs) -> dict:
        event = LogEvent(message=message, level=LogLevel.DEBUG)
        logging.debug(str(event))
        return event.dict()

    def info(self, message: str, **kwargs) -> dict:
        event = LogEvent(message=message, level=LogLevel.INFO)
        logging.info(str(event))
        return event.dict()

    def warning(self, message: str, **kwargs) -> dict:
        event = LogEvent(message=message, level=LogLevel.WARNING)
        logging.warning(str(event))
        return event.dict()

    def error(self, message: str, **kwargs) -> dict:
        event = LogEvent(message=message, level=LogLevel.WARNING)
        logging.warning(str(event))
        return event.dict()