import logging

from .settings import auto_config as cfg

if not cfg:
    raise RuntimeError(
        "configuration is not set. Please set the ENVIRONMENT environment variable."
    )


logging.basicConfig(
    level=getattr(logging, cfg.LOG_LEVEL.upper()), format=cfg.LOG_FORMAT
)

logger = logging.getLogger(cfg.MCP_SERVER_NAME)
