FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_CACHE_DIR=/tmp/uv-cache

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

COPY . .

RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app && \
    mkdir -p /tmp/uv-cache && \
    chown -R app:app /tmp/uv-cache
USER app

EXPOSE 8000

CMD ["uv", "run", "--no-dev", "fastmcp", "run", "--transport", "sse", "mcp_server/app.py:mcp"] 