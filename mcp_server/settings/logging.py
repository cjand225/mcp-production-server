"""Logging configuration and utilities."""

import logging

from fastmcp.utilities.logging import get_logger

from .config import Config


def get_app_logger() -> logging.Logger:
    """
    Configure the FastMCP framework logger with application settings.

    Returns:
        FastMCP logger configured with application settings.
    """
    logger = get_logger("FastMCP")

    logger.setLevel(getattr(logging, Config.LOG_LEVEL))

    for handler in logger.handlers:
        formatter = logging.Formatter(Config.LOG_FORMAT)
        handler.setFormatter(formatter)
        handler.setLevel(getattr(logging, Config.LOG_LEVEL))

    return logger
