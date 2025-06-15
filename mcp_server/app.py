"""FastMCP application instance."""

from fastmcp import FastMCP

from mcp_server.settings import Config as cfg
from mcp_server.settings.logging import get_app_logger

logger = get_app_logger()

mcp: FastMCP = FastMCP(
    name=cfg.MCP_SERVER_NAME,
    host=cfg.HOST,
    port=cfg.PORT,
    log_level=cfg.LOG_LEVEL,
)
