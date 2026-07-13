import logging
from typing import Literal

import structlog
from pydantic import BaseModel


class LoggingConfig(BaseModel):
    level: str = "INFO"
    renderer: Literal["console", "json"] = "console"


def setup_logging(logging_config: LoggingConfig):
    """Setup logging based on the provided configuration."""
    level = logging_config.level.upper()

    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
    )

    renderer = (
        structlog.processors.JSONRenderer()
        if logging_config.renderer == "json"
        else structlog.dev.ConsoleRenderer()
    )

    formatter = structlog.stdlib.ProcessorFormatter(processor=renderer)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logging.basicConfig(handlers=[handler], level=level, force=True)

    return structlog.get_logger()


def get_logger(name: str):
    """Get a logger with the specified name."""
    return structlog.get_logger(name)
