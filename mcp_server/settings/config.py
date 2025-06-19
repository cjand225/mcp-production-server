import os


class Config:
    """Single configuration class with environment variable overrides"""

    # Static MCP Server Settings
    MCP_SERVER_NAME: str = "mcp-production"
    MCP_SERVER_VERSION: str = "0.1.0"

    # Environment-configurable settings with defaults
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # Transport: stdio for MCP, sse for HTTP deployment
    TRANSPORT: str = os.getenv("TRANSPORT", "sse")

    # Logging configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
    LOG_FORMAT: str = os.getenv(
        "LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # JWT Authentication Settings
    JWT_PUBLIC_KEY: str = os.getenv("JWT_PUBLIC_KEY", "")
    JWKS_URI: str = os.getenv("JWKS_URI", "")
    JWT_ISSUER: str = os.getenv("JWT_ISSUER", "")
    JWT_AUDIENCE: str = os.getenv("JWT_AUDIENCE", "")
    REQUIRED_SCOPES: list[str] = (
        os.getenv("REQUIRED_SCOPES", "").split(",")
        if os.getenv("REQUIRED_SCOPES")
        else []
    )

    @classmethod
    def is_production(cls) -> bool:
        """Helper method to check if running in production mode"""
        return os.getenv("ENVIRONMENT", "development").lower() == "production"

    @classmethod
    def is_debug(cls) -> bool:
        """Helper method to check debug status"""
        return cls.DEBUG
