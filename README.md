# MCP Production Server

A production-ready server for building Model Context Protocol (MCP) servers in Python, featuring modules for tools, resources, prompts, JWT authentication, and flexible deployment options.

## Features

### Core Capabilities
- **Modular Architecture**: Support for tools, resources, and prompts
- **JWT Authentication**: Secure Bearer token validation with RS256 encryption
- **Multiple Transports**: Support for stdio, SSE, and streamable HTTP
- **Environment Configuration**: Fully configurable via environment variables

### Technical Features
- **Production Ready**: Comprehensive logging, error handling, and Docker support
- **FastMCP Integration**: Built on the FastMCP framework
- **Flexible Deployment**: Docker, direct execution, and multiple transport options

## Quick Start

### Prerequisites
- Python 3.12+
- uv

### Installation and Running
```bash
# Clone the repository
git clone <repository-url>
cd mcp-production

# Install dependencies
uv sync

# Run with SSE transport (for web-based clients)
uv run fastmcp run --transport sse mcp_server/app.py:mcp

# Or run with stdio transport (for direct MCP clients)
uv run fastmcp run --transport stdio mcp_server/app.py:mcp

# For production with Docker Compose
docker-compose up -d

# Or build and run with Docker directly
# (build the image)
docker build -t mcp-production .
# run the image
docker run -p 8000:8000 -e JWT_PUBLIC_KEY="..." mcp-production
```

## Configuration

### Environment Variables

See [`.env.example`](./.env.example) for a complete configuration template.

```bash
# Server Configuration
MCP_SERVER_NAME=mcp-production
DEBUG=false
HOST=0.0.0.0
PORT=8000
TRANSPORT=sse
LOG_LEVEL=INFO

# JWT Authentication (Optional)
JWT_PUBLIC_KEY="-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
-----END PUBLIC KEY-----"

# Or use JWKS URI
JWKS_URI=https://your-auth-provider.com/.well-known/jwks.json

# JWT Validation Settings
JWT_ISSUER=https://your-auth-provider.com
JWT_AUDIENCE=your-mcp-server
REQUIRED_SCOPES=read,write
```

#### JWT Authentication

The server supports JWT Bearer token authentication with RS256 encryption. Choose one configuration method:

**Static Public Key** (for development/testing):
```bash
JWT_PUBLIC_KEY="-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----"
JWT_ISSUER=https://your-auth-provider.com
```

**JWKS URI** (recommended for production):
```bash
JWKS_URI=https://your-auth-provider.com/.well-known/jwks.json
JWT_ISSUER=https://your-auth-provider.com
```

**Generate test token** for development:
```python
from mcp_server.auth import create_test_token
token = create_test_token()
```

#### Transport Options

- **stdio**: Standard input/output (for direct MCP client connections)
- **sse**: Server-Sent Events (for web-based clients)
- **streamable-http**: HTTP streaming (for REST-like integrations)

## Tools

TBD

## Resources

TBD

## Prompts

TBD

## Related Links

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [FastMCP Framework](https://github.com/jlowin/fastmcp)
- [JWT.io](https://jwt.io/) - JWT token debugging
