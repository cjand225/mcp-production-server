import os

from .config import Common, Local, Production, Staging

environment: str | None = os.getenv("ENVIRONMENT", None)

if not environment:
    raise EnvironmentError("ENVIRONMENT environment variable is not set!")

auto_config: type[Common] | None = None
if environment == "local":
    auto_config = Local
elif environment == "staging":
    auto_config = Staging
elif environment == "production":
    auto_config = Production


if not auto_config:
    raise RuntimeError(
        "Configuration is not set. Please set the ENVIRONMENT environment variable."
    )
