"""Text processing resources for MCP Server."""

from typing import Any, Dict


def text_stats_resource():
    """Text processing statistics resource."""
    # This could track usage statistics, performance metrics, etc.
    return {
        "success": True,
        "stats": {
            "total_operations": 0,
            "most_used_tools": [],
            "average_text_length": 0,
            "supported_operations": [
                "case transformation",
                "text analysis",
                "text cleaning",
                "pattern extraction",
                "encoding/decoding",
                "text formatting",
            ],
        },
    }


def supported_encodings_resource():
    """Supported encodings resource."""
    return {
        "success": True,
        "encodings": {
            "encoding_methods": ["base64", "url", "html", "hex", "md5", "sha256"],
            "decoding_methods": ["base64", "url", "html", "hex"],
            "hash_methods": ["md5", "sha256"],
        },
    }


def supported_patterns_resource():
    """Supported patterns resource."""
    return {
        "success": True,
        "patterns": {
            "contact_patterns": ["email", "phone"],
            "web_patterns": ["url", "ip"],
            "text_patterns": ["word", "number"],
            "social_patterns": ["hashtag", "mention"],
            "all_patterns": [
                "email",
                "url",
                "phone",
                "number",
                "word",
                "hashtag",
                "mention",
                "ip",
            ],
        },
    }


def case_types_resource():
    """Case transformation types resource."""
    return {
        "success": True,
        "case_types": {
            "basic_cases": ["upper", "lower", "title", "capitalize"],
            "programming_cases": ["camel", "pascal", "snake", "kebab", "constant"],
            "all_cases": [
                "upper",
                "lower",
                "title",
                "capitalize",
                "camel",
                "pascal",
                "snake",
                "kebab",
                "constant",
            ],
        },
    }


def format_operations_resource():
    """Text formatting operations resource."""
    return {
        "success": True,
        "operations": {
            "layout_operations": ["wrap", "indent", "center", "ljust", "rjust"],
            "transformation_operations": ["reverse", "sort_lines", "reverse_lines"],
            "all_operations": [
                "wrap",
                "indent",
                "center",
                "ljust",
                "rjust",
                "reverse",
                "sort_lines",
                "reverse_lines",
            ],
        },
    }


def cleaning_options_resource():
    """Text cleaning options resource."""
    return {
        "success": True,
        "cleaning_options": {
            "content_removal": [
                "remove_html",
                "remove_urls",
                "remove_emails",
                "remove_special_chars",
            ],
            "formatting_options": ["remove_extra_spaces", "normalize_unicode"],
            "all_options": [
                "remove_extra_spaces",
                "remove_special_chars",
                "normalize_unicode",
                "remove_html",
                "remove_urls",
                "remove_emails",
            ],
        },
    }


def text_examples_resource():
    """Text examples resource."""
    pass


def style_guide_resource():
    """Style guide resource."""
    pass


def get_text_resource_info() -> Dict[str, Any]:
    """Get information about available text processing resources.

    Returns:
        Dictionary containing resource information
    """
    return {
        "resource_count": 6,
        "resources": [
            {
                "name": "text_stats",
                "description": "Comprehensive statistics about text processing operations",
                "type": "statistics",
            },
            {
                "name": "text_supported_encodings",
                "description": "List of supported encoding methods",
                "type": "reference",
            },
            {
                "name": "text_supported_patterns",
                "description": "List of supported pattern types for extraction",
                "type": "reference",
            },
            {
                "name": "text_case_types",
                "description": "List of supported case transformation types",
                "type": "reference",
            },
            {
                "name": "text_format_operations",
                "description": "List of supported text formatting operations",
                "type": "reference",
            },
            {
                "name": "text_cleaning_options",
                "description": "List of available text cleaning options",
                "type": "reference",
            },
        ],
    }
