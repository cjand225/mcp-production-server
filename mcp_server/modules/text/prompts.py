"""Text processing prompts for MCP Server."""


def summarize_prompt():
    """Summarize text prompt."""
    return (
        "Please provide a concise summary of the following text:\n\n{text}\n\nSummary:"
    )


def improve_text_prompt():
    """Improve text prompt."""
    return (
        "Please improve the following text for clarity, grammar, and style:\n\n"
        "{text}\n\n"
        "Improved version:"
    )


def extract_key_points_prompt():
    """Extract key points prompt."""
    return (
        "Please extract the key points from the following text:\n\n"
        "{text}\n\n"
        "Key points:"
    )


def translate_text_prompt():
    """Translate text prompt."""
    return (
        "Please translate the following text from {source_language} to {target_language}:\n\n"
        "{text}\n\n"
        "Translation:"
    )


def generate_questions_prompt():
    """Generate questions prompt."""
    return (
        "Based on the following text, generate 3-5 thought-provoking questions:\n\n"
        "{text}\n\n"
        "Questions:"
    )


def paraphrase_text_prompt():
    """Paraphrase text prompt."""
    return (
        "Please paraphrase the following text while maintaining its original meaning:\n\n"
        "{text}\n\n"
        "Paraphrased version:"
    )


def extract_keywords_prompt():
    """Extract keywords prompt."""
    return "Extract the main keywords and topics from the following text:\n\n{text}\n\nKeywords:"


def sentiment_analysis_prompt():
    """Sentiment analysis prompt."""
    return "Analyze the sentiment (positive, negative, neutral) of the following text and provide reasoning:\n\n{text}\n\nSentiment Analysis:"


def grammar_check_prompt():
    """Grammar check prompt."""
    return "Check the following text for grammar errors and provide corrections:\n\n{text}\n\nGrammar Check:"


def text_explanation_prompt():
    """Text explanation prompt."""
    return "Explain the following text in simple, easy-to-understand language:\n\n{text}\n\nSimple Explanation:"


def generate_outline_prompt():
    """Generate outline prompt."""
    return "Create a structured outline from the following text:\n\n{text}\n\nOutline:"
