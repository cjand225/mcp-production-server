from mcp.server.fastmcp import FastMCP

from .logging import logger
from .settings import auto_config as cfg

if not cfg:
    raise RuntimeError(
        "configuration is not set. Please set the ENVIRONMENT environment variable."
    )

mcp = FastMCP(name=cfg.MCP_SERVER_NAME, transport=cfg.TRANSPORT)

logger.info(f"Starting {cfg.MCP_SERVER_NAME} v{cfg.MCP_SERVER_VERSION}")
logger.debug(f"Debug mode: {cfg.DEBUG}")
logger.info(f"Base URL: {cfg.BASE_URL}")
logger.debug(f"Log level: {cfg.LOG_LEVEL}")
