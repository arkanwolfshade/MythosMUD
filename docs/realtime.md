# Real-Time Communication (WebSocket)

This document covers WebSocket authentication, security considerations, and production
deployment for MythosMUD real-time communication. See ADR-004 for the decision to use
WebSocket-only for real-time traffic.

## Authentication and Token in URL

The client sends the JWT (or session token) in the WebSocket URL query string (e.g.
`/api/ws?token=...&session_id=...`). This is a **known trade-off**:

- **Reason**: JWT format (e.g. dots, base64) is incompatible with the WebSocket
  subprotocol header, so the subprotocol cannot carry the token. The query string is
  the supported alternative for the initial handshake.
- **Security**: Over **HTTPS**, the URL is encrypted in transit. To reduce risk:
  - Use **short-lived** access tokens for WebSocket connections.
  - Ensure server **access logs do not log query strings** for the WebSocket path
    (or redact the token). Configure logging accordingly in production.
- **Optional improvement**: A one-time connection token exchanged via a secure REST
  call could be used in the WebSocket URL instead of the JWT; that would limit
  exposure if the WebSocket URL were ever logged or leaked.

## Production: HTTPS and WSS

**Production deployments must serve the application over HTTPS.** When the application
is loaded over HTTPS, the browser will use **WSS** (secure WebSocket) for the same
origin; credentials and traffic remain protected in transit.

- Configure TLS/HTTPS for the HTTP server (e.g. Gunicorn/Uvicorn with TLS, or a
  reverse proxy terminating TLS).
- Do not serve the game over plain HTTP in production; otherwise WebSocket
  connections use `ws://` and are unencrypted.

See [deployment.md](deployment.md) for production server setup.

## Deprecated Endpoints

- **`GET /api/ws/{player_id}`**: Deprecated. Use `GET /api/ws` with JWT (query param or
  subprotocol) and optional `session_id` and `character_id` instead. This route will
  be removed in a future release. Validation matches the primary route (async persistence).
