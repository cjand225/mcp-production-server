"""Text Processing Module for MCP Server.

This module provides comprehensive text processing capabilities including:
- Text transformation and formatting
- String analysis and metrics
- Text cleaning and normalization
- Content extraction and manipulation
"""

# Import the modules to register their decorators with FastMCP
from . import prompts, resources, tools

__all__ = ["tools", "prompts", "resources"]
