"""Helper functions for text processing operations."""

import re


def to_camel_case(text: str) -> str:
    """Convert text to camelCase."""
    words = re.split(r"[\s_-]+", text.strip())
    if not words:
        return ""
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def to_pascal_case(text: str) -> str:
    """Convert text to PascalCase."""
    words = re.split(r"[\s_-]+", text.strip())
    return "".join(word.capitalize() for word in words)


def to_snake_case(text: str) -> str:
    """Convert text to snake_case."""
    # Handle camelCase and PascalCase
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    # Replace spaces and hyphens with underscores
    text = re.sub(r"[\s-]+", "_", text)
    return text.lower()


def to_kebab_case(text: str) -> str:
    """Convert text to kebab-case."""
    # Handle camelCase and PascalCase
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", text)
    # Replace spaces and underscores with hyphens
    text = re.sub(r"[\s_]+", "-", text)
    return text.lower()


def to_constant_case(text: str) -> str:
    """Convert text to CONSTANT_CASE."""
    return to_snake_case(text).upper()
