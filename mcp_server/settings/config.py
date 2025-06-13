import os


class Common:
    """Base configuration class with common settings"""

    # MCP Server Settings
    MCP_SERVER_NAME: str = "mcp-production"
    MCP_SERVER_VERSION: str = "0.1.0"
    TRANSPORT: str = "stdio"

    # Application Settings
    DEBUG: bool = False
    BASE_URL: str = "http://localhost:8000"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class Local(Common):
    """Local development configuration"""

    DEBUG: bool = True
    LOG_LEVEL: str = os.getenv("SERVER_LOG_LEVEL", "DEBUG")
    BASE_URL: str = "http://localhost:8000"


class Production(Common):
    """Production configuration"""

    DEBUG: bool = False
    LOG_LEVEL: str = os.getenv("SERVER_LOG_LEVEL", "WARNING")
    BASE_URL: str = os.getenv("PRODUCTION_BASE_URL", "https://api.production.com")


class Staging(Production):
    """Staging configuration - inherits from Production but with debug enabled"""

    DEBUG: bool = True
    LOG_LEVEL: str = os.getenv("SERVER_LOG_LEVEL", "INFO")
    BASE_URL: str = os.getenv("STAGING_BASE_URL", "https://api.staging.com")
