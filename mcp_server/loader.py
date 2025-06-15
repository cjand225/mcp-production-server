"""Module loader for MCP Server.

This module handles the loading and registration of all MCP server modules
including tools, prompts, and resources.
"""

from fastmcp import FastMCP


def register_tools(app: FastMCP) -> None:
    """Register text processing tools with the application."""
    from mcp_server.modules.text import tools

    app.tool(
        name="text_transform_case",
        description="Transform text case (upper, lower, title, camel, snake, etc.)",
    )(tools.transform_case)

    app.tool(
        name="text_analyze_text", description="Analyze text and provide statistics"
    )(tools.analyze_text)

    app.tool(name="text_clean_text", description="Clean and normalize text")(
        tools.clean_text
    )

    app.tool(
        name="text_extract_patterns",
        description="Extract patterns like emails, URLs, phone numbers from text",
    )(tools.extract_patterns)

    app.tool(
        name="text_encode_text",
        description="Encode text using various encoding methods",
    )(tools.encode_text)

    app.tool(
        name="text_format_text",
        description="Format text with various formatting options",
    )(tools.format_text)


def register_resources(app: FastMCP) -> None:
    """Register text processing resources with the application."""
    from mcp_server.modules.text import resources

    app.resource(
        name="text_stats",
        uri="internal://text/stats",
        description="Comprehensive statistics about text processing operations",
        mime_type="application/json",
    )(resources.text_stats_resource)

    app.resource(
        name="text_case_types",
        uri="internal://text/case-types",
        description="List of supported case transformation types",
        mime_type="application/json",
    )(resources.case_types_resource)

    app.resource(
        name="text_format_operations",
        uri="internal://text/format-operations",
        description="List of supported text formatting operations",
        mime_type="application/json",
    )(resources.format_operations_resource)

    app.resource(
        name="text_cleaning_options",
        uri="internal://text/cleaning-options",
        description="List of available text cleaning options",
        mime_type="application/json",
    )(resources.cleaning_options_resource)


def register_prompts(app: FastMCP) -> None:
    """Register text processing prompts with the application."""
    from mcp_server.modules.text import prompts

    app.prompt(
        name="text_summarize", description="Generate a summary of the given text"
    )(prompts.summarize_prompt)

    app.prompt(
        name="text_improve_writing", description="Improve the writing quality of text"
    )(prompts.improve_text_prompt)

    app.prompt(
        name="text_extract_keywords",
        description="Extract key topics and keywords from text",
    )(prompts.extract_keywords_prompt)

    app.prompt(
        name="text_sentiment_analysis", description="Analyze the sentiment of text"
    )(prompts.sentiment_analysis_prompt)

    app.prompt(
        name="text_grammar_check", description="Check and correct grammar in text"
    )(prompts.grammar_check_prompt)

    app.prompt(
        name="text_explanation", description="Explain complex text in simple terms"
    )(prompts.text_explanation_prompt)

    app.prompt(
        name="text_generate_outline",
        description="Generate an outline from text content",
    )(prompts.generate_outline_prompt)


def load_modules(app: FastMCP) -> None:
    """
    Load and register all MCP server modules with the application.

    Args:
        app: The FastMCP application instance to register modules with.
    """
    register_tools(app)
    register_resources(app)
    register_prompts(app)
