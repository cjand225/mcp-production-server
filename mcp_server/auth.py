"""Authentication configuration for MCP Server."""

from typing import Optional

from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.auth import OAuthProvider

from mcp_server.settings import Config as cfg
from mcp_server.settings.logging import get_app_logger

logger = get_app_logger("mcp_server.auth")


def get_auth_provider() -> Optional[OAuthProvider]:
    """
    Configure and return the appropriate authentication provider based on settings.

    Returns:
        Configured OAuthProvider instance if auth settings are available, None otherwise.
    """
    # Check for static public key configuration
    jwt_public_key = getattr(cfg, "JWT_PUBLIC_KEY", None) or ""
    jwks_uri = getattr(cfg, "JWKS_URI", None) or ""

    if jwt_public_key:
        # Using static public key
        auth_provider = BearerAuthProvider(
            public_key=jwt_public_key,
            issuer=getattr(cfg, "JWT_ISSUER", None),
            audience=getattr(cfg, "JWT_AUDIENCE", None),
            required_scopes=getattr(cfg, "REQUIRED_SCOPES", None),
        )
        logger.info("Configured JWT auth with static public key")
        return auth_provider

    elif jwks_uri:
        auth_provider = BearerAuthProvider(
            jwks_uri=jwks_uri,
            issuer=getattr(cfg, "JWT_ISSUER", None),
            audience=getattr(cfg, "JWT_AUDIENCE", None),
            required_scopes=getattr(cfg, "REQUIRED_SCOPES", None),
        )
        logger.info(f"Configured JWT auth with JWKS URI: {jwks_uri}")
        return auth_provider

    else:
        logger.warning(
            "No JWT auth configuration found - server will run without authentication"
        )
        return None


def create_test_token() -> str:
    """
    Create a test JWT token for development/testing purposes.
    This function generates a key pair and creates a signed token.

    Returns:
        A valid JWT token string for testing.
    """
    from fastmcp.server.auth.providers.bearer import RSAKeyPair

    # Generate a key pair for testing
    key_pair = RSAKeyPair.generate()

    # Create a test token
    token = key_pair.create_token(
        subject="test-user",
        issuer="https://fastmcp.example.com",
        scopes=["read", "write"],
        expires_in_seconds=3600,
    )

    logger.info("Generated test JWT token")
    logger.info(f"Public key for verification:\n{key_pair.public_key}")

    return token
