# MythosMUD Deployment

## Production: HTTPS and WSS

Production must be served over **HTTPS** so that WebSocket connections use **WSS**
(secure WebSocket) and credentials remain protected. Configure TLS at the server or
reverse proxy; see [realtime.md](realtime.md) for details.

## Production: Gunicorn + Uvicorn

For production, run the ASGI app with **Gunicorn** as the process manager and **Uvicorn** as the worker
class. This provides multiple worker processes and proper request handling.

### From project root

- **Makefile:** `make run-production` (binds to 0.0.0.0:8000).
- **Manual:** `uv run gunicorn server.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000`

For a different port, use `-b 0.0.0.0:PORT` in the manual command.

- `-w 4`: 4 worker processes (tune for CPU cores).
- `-k uvicorn.workers.UvicornWorker`: Use Uvicorn's ASGI worker.
- `-b 0.0.0.0:8000`: Bind to all interfaces on port 8000.

### Health checks

- System health: `GET /v1/health`
- Comprehensive health: `GET /v1/monitoring/health`

Use these URLs for load balancers and orchestration health checks.

### Stopping the server

Use `./scripts/stop_server.ps1` (Windows) to stop both Uvicorn and Gunicorn server processes.

### NATS (optional)

For NATS servers that require authentication, set `NATS_USER` and `NATS_PASSWORD`, or
`NATS_TOKEN`, via environment or secrets manager (see env.\*.example NATS sections).
For local development with NATS over TLS, generate certs with
`./scripts/generate_nats_local_certs.ps1` (output in `certs/nats/`); then set
`NATS_TLS_ENABLED`, `NATS_TLS_CERT_FILE`, `NATS_TLS_KEY_FILE`, and `NATS_TLS_CA_FILE`
in `.env.local`.

### Development

Local development continues to use Uvicorn only (e.g. `scripts/start_server.ps1` or
`make run`). Gunicorn is not required for development.
