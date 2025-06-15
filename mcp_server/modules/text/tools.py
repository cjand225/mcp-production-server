"""Text processing tools for MCP Server."""

import hashlib
import re
import urllib.parse
from typing import Any, Dict

from .helpers import (
    to_camel_case,
    to_constant_case,
    to_kebab_case,
    to_pascal_case,
    to_snake_case,
)


async def transform_case(text: str, case_type: str) -> Dict[str, Any]:
    """Transform text case.

    Args:
        text: Input text to transform
        case_type: Type of case transformation (upper, lower, title, camel, snake, kebab, pascal)
    """
    try:
        case_type = case_type.lower().strip()

        transformations = {
            "upper": text.upper(),
            "lower": text.lower(),
            "title": text.title(),
            "capitalize": text.capitalize(),
            "camel": to_camel_case(text),
            "pascal": to_pascal_case(text),
            "snake": to_snake_case(text),
            "kebab": to_kebab_case(text),
            "constant": to_constant_case(text),
        }

        if case_type not in transformations:
            return {
                "success": False,
                "error": f"Unsupported case type: {case_type}. Available: {', '.join(transformations.keys())}",
            }

        result = transformations[case_type]
        return {
            "success": True,
            "original": text,
            "transformed": result,
            "case_type": case_type,
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Case transformation failed: {str(e)}",
        }


async def analyze_text(text: str) -> Dict[str, Any]:
    """Analyze text and provide statistics.

    Args:
        text: Input text to analyze
    """
    try:
        words = text.split()
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if s.strip()]

        # Character analysis
        char_counts = {
            "total": len(text),
            "letters": sum(1 for c in text if c.isalpha()),
            "digits": sum(1 for c in text if c.isdigit()),
            "spaces": sum(1 for c in text if c.isspace()),
            "punctuation": sum(1 for c in text if not c.isalnum() and not c.isspace()),
        }

        return {
            "success": True,
            "analysis": {
                "word_count": len(words),
                "sentence_count": len(sentences),
                "character_counts": char_counts,
                "average_word_length": sum(len(word) for word in words) / len(words)
                if words
                else 0,
                "average_sentence_length": len(words) / len(sentences)
                if sentences
                else 0,
            },
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Text analysis failed: {str(e)}",
        }


async def clean_text(
    text: str,
    remove_html: bool = True,
    remove_urls: bool = True,
    normalize_whitespace: bool = True,
) -> Dict[str, Any]:
    """Clean and normalize text.

    Args:
        text: Input text to clean
        remove_html: Whether to remove HTML tags
        remove_urls: Whether to remove URLs
        normalize_whitespace: Whether to normalize whitespace
    """
    try:
        cleaned = text

        if remove_html:
            # Remove HTML tags
            cleaned = re.sub(r"<[^>]+>", "", cleaned)

        if remove_urls:
            # Remove URLs
            url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
            cleaned = re.sub(url_pattern, "", cleaned)

        if normalize_whitespace:
            # Normalize whitespace
            cleaned = re.sub(r"\s+", " ", cleaned).strip()

        return {
            "success": True,
            "original": text,
            "cleaned": cleaned,
            "operations": {
                "remove_html": remove_html,
                "remove_urls": remove_urls,
                "normalize_whitespace": normalize_whitespace,
            },
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Text cleaning failed: {str(e)}",
        }


async def extract_patterns(text: str, pattern_type: str = "all") -> Dict[str, Any]:
    """Extract patterns from text.

    Args:
        text: Input text to search
        pattern_type: Type of pattern to extract (email, url, phone, hashtag, mention, ip, all)
    """
    try:
        patterns = {
            "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "url": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            "phone": r"(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})",
            "hashtag": r"#\w+",
            "mention": r"@\w+",
            "ip": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
        }

        results = {}

        if pattern_type.lower() == "all":
            for name, pattern in patterns.items():
                matches = re.findall(pattern, text)
                results[name] = matches
        elif pattern_type.lower() in patterns:
            pattern = patterns[pattern_type.lower()]
            matches = re.findall(pattern, text)
            results[pattern_type.lower()] = matches
        else:
            return {
                "success": False,
                "error": f"Unsupported pattern type: {pattern_type}. Available: {', '.join(patterns.keys())}, all",
            }

        return {
            "success": True,
            "pattern_type": pattern_type,
            "results": results,
            "total_matches": sum(len(matches) for matches in results.values()),
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Pattern extraction failed: {str(e)}",
        }


async def encode_text(text: str, encoding_type: str) -> Dict[str, Any]:
    """Encode text using various methods.

    Args:
        text: Input text to encode
        encoding_type: Type of encoding (base64, url, html, hex, md5, sha256)
    """
    try:
        import base64
        import html

        encoding_type = encoding_type.lower().strip()

        encodings = {
            "base64": lambda t: base64.b64encode(t.encode("utf-8")).decode("utf-8"),
            "url": lambda t: urllib.parse.quote(t),
            "html": lambda t: html.escape(t),
            "hex": lambda t: t.encode("utf-8").hex(),
            "md5": lambda t: hashlib.md5(t.encode("utf-8")).hexdigest(),
            "sha256": lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest(),
        }

        if encoding_type not in encodings:
            return {
                "success": False,
                "error": f"Unsupported encoding type: {encoding_type}. Available: {', '.join(encodings.keys())}",
            }

        encoded = encodings[encoding_type](text)
        return {
            "success": True,
            "original": text,
            "encoded": encoded,
            "encoding_type": encoding_type,
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Text encoding failed: {str(e)}",
        }


async def format_text(text: str, format_type: str, width: int = 80) -> Dict[str, Any]:
    """Format text with various options.

    Args:
        text: Input text to format
        format_type: Type of formatting (wrap, indent, center, justify, reverse, sort_lines)
        width: Width for formatting operations (default: 80)
    """
    try:
        import textwrap

        format_type = format_type.lower().strip()

        formatters = {
            "wrap": lambda t, w: textwrap.fill(t, width=w),
            "indent": lambda t, w: textwrap.indent(t, "    "),
            "center": lambda t, w: "\n".join(line.center(w) for line in t.split("\n")),
            "justify": lambda t, w: textwrap.fill(
                t, width=w, expand_tabs=True, replace_whitespace=True
            ),
            "reverse": lambda t, w: t[::-1],
            "sort_lines": lambda t, w: "\n".join(sorted(t.split("\n"))),
        }

        if format_type not in formatters:
            return {
                "success": False,
                "error": f"Unsupported format type: {format_type}. Available: {', '.join(formatters.keys())}",
            }

        formatted = formatters[format_type](text, width)
        return {
            "success": True,
            "original": text,
            "formatted": formatted,
            "format_type": format_type,
            "width": width,
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Text formatting failed: {str(e)}",
        }
