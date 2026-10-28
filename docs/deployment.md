# MythosMUD Deployment

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Production: HTTPS and WSS

**[NOTE]**
Production must be served over **HTTPS** so that WebSocket connections use **WSS**
(secure WebSocket) and credentials remain protected. Configure TLS at the server or
reverse proxy; see [realtime.md](realtime.md) for details.

## 2. Supported deployment: single-process Uvicorn

**[SPEC]**
MythosMUD supports exactly one deployment mode: **one Uvicorn process**. Gunicorn and multi-worker
setups are unsupported.

**[NOTE]**
Connections, the shutdown flag and other game state live in the process's `app.state`. A second worker would
be a separate world, and a process supervisor that respawns the worker would undo the admin `shutdown`
command (#1146). Run `make run`, or `uv run uvicorn server.main:app --host 0.0.0.0 --port 8000`. Restart
policy, if wanted, belongs to the host (systemd, container runtime) and must not restart after a clean exit.

### Health checks

- System health: `GET /v1/health`
- Comprehensive health: `GET /v1/monitoring/health`

Use these URLs for load balancers and orchestration health checks.

### Stopping the server

Use `./scripts/stop_server.ps1` (Windows) to stop the server process.

### NATS (optional)

For NATS servers that require authentication, set `NATS_USER` and `NATS_PASSWORD`, or
`NATS_TOKEN`, via environment or secrets manager (see env.\*.example NATS sections).
For local development with NATS over TLS, generate certs with
`./scripts/generate_nats_local_certs.ps1` (output in `certs/nats/`); then set
`NATS_TLS_ENABLED`, `NATS_TLS_CERT_FILE`, `NATS_TLS_KEY_FILE`, and `NATS_TLS_CA_FILE`
in `.env.local`.

## 3. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
