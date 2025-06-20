"""Logging configuration and utilities."""

import logging
import re
import sys

from rich.console import Console
from rich.logging import RichHandler

from .config import Config


class RichLoggingHandler(logging.StreamHandler):
    """Custom logging handler that provides Rich-based colored output with consistent formatting."""

    def __init__(self):
        super().__init__(sys.stdout)

        self.console = Console(file=sys.stdout, force_terminal=True)
        self.rich_handler = RichHandler(
            console=self.console,
            show_time=True,
            show_level=True,
            show_path=False,
            omit_repeated_times=False,
            markup=False,
            rich_tracebacks=True,
            tracebacks_show_locals=False,
        )
        self.rich_handler.setFormatter(logging.Formatter("%(message)s"))

    def emit(self, record):
        try:
            original_msg = str(record.getMessage())

            # Parse uvicorn format: "INFO: message"
            uvicorn_pattern = re.match(
                r"^(INFO|ERROR|WARNING|DEBUG):\s*(.*)$", original_msg
            )
            if uvicorn_pattern:
                level = uvicorn_pattern.group(1)
                message = uvicorn_pattern.group(2).strip()
                record.msg = message
                record.levelname = level
                record.levelno = getattr(logging, level)

            # Parse bracket format: "[timestamp] LEVEL message"
            elif original_msg.startswith("[") and (
                "] INFO" in original_msg
                or "] ERROR" in original_msg
                or "] WARNING" in original_msg
                or "] DEBUG" in original_msg
            ):
                for level in ["INFO", "ERROR", "WARNING", "DEBUG"]:
                    if f"] {level}" in original_msg:
                        bracket_match = re.search(rf"\]\s*{level}\s*(.*)", original_msg)
                        if bracket_match:
                            record.msg = bracket_match.group(1).strip()
                            record.levelname = level
                            record.levelno = getattr(logging, level)
                            break

            # Parse format: "logger - LEVEL - message"
            elif " - " in original_msg and any(
                level in original_msg for level in ["INFO", "ERROR", "WARNING", "DEBUG"]
            ):
                parts = original_msg.split(" - ", 2)
                if len(parts) >= 3:
                    logger_name, level, message = parts
                    if level in ["INFO", "ERROR", "WARNING", "DEBUG"]:
                        record.msg = message.strip()
                        record.levelname = level
                        record.levelno = getattr(logging, level)

            record.msg = str(record.msg).replace("\n", " ").strip()
            self.rich_handler.emit(record)

        except Exception:
            super().emit(record)


def configure_logging() -> None:
    """Configure application logging using Rich for colored output."""

    handler = RichLoggingHandler()
    handler.setLevel(logging.DEBUG)

    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)

    logger_names = [
        # Uvicorn
        "uvicorn",
        "uvicorn.error",
        "uvicorn.access",
        # FastMCP framework
        "FastMCP",
        "fastmcp",
        # MCP server
        "mcp.server.lowlevel.server",
        "mcp.server.sse",
        "mcp.server.fastmcp.server",
        "mcp.server.fastmcp.tools.tool_manager",
        "mcp.server.fastmcp.resources.resource_manager",
        "mcp.server.fastmcp.prompts.manager",
        # Application
        "mcp_server",
        "mcp_server.auth",
        "mcp_server.app",
        # System loggers
        "asyncio",
        "rich",
        "httpx",
    ]

    for logger_name in logger_names:
        logger = logging.getLogger(logger_name)
        logger.addHandler(handler)
        logger.setLevel(getattr(logging, Config.LOG_LEVEL))
        logger.propagate = False  # Prevent double logging


def get_app_logger(name: str = "mcp_server") -> logging.Logger:
    """Get a configured logger for the application."""
    logger = logging.getLogger(name)

    handler = RichLoggingHandler()
    handler.setLevel(getattr(logging, Config.LOG_LEVEL))

    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, Config.LOG_LEVEL))
    logger.propagate = False

    return logger


configure_logging()
