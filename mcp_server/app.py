"""FastMCP application instance."""

from fastmcp import FastMCP

from mcp_server.auth import get_auth_provider
from mcp_server.loader import load_modules
from mcp_server.settings import Config as cfg
from mcp_server.settings.logging import get_app_logger

logger = get_app_logger("mcp_server.app")

auth_provider = get_auth_provider()

mcp: FastMCP = FastMCP(
    name=cfg.MCP_SERVER_NAME,
    host=cfg.HOST,
    port=cfg.PORT,
    log_level=cfg.LOG_LEVEL,
    auth=auth_provider,
)

load_modules(mcp)
