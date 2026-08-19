# API OpenAPI/Swagger Specification

**Version 1.1.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Document Version:** 1.0
**Date:** February 2026
**Status:** Architecture documentation
**Purpose:** Document API contracts and service interfaces with OpenAPI/Swagger per Architecture Review Plan.

---

## 2. Overview

**[SPEC]**
MythosMUD exposes a REST API and WebSocket interface for the Cthulhu Mythos-themed MUD client. This document describes how API contracts are documented and how to use the OpenAPI specification.

### 2.1 OpenAPI Specification

- **Format:** OpenAPI 3.1.0
- **Location:** `docs/openapi/openapi.json`
- **Source of truth:** Generated from the FastAPI application at runtime.

### 2.2 Interactive Documentation

When the server is running:

| UI | URL | Description |
|----|-----|-------------|
| Swagger UI | `/docs` | Interactive API explorer; try endpoints, view schemas |
| ReDoc | `/redoc` | Alternative documentation UI |
| OpenAPI JSON | `/openapi.json` | Raw OpenAPI schema |

---

## 3. Generating the OpenAPI Spec

**[SPEC]**
The specification is generated from the live FastAPI application. Run:

```powershell
uv run python scripts/generate_openapi_spec.py
```

Or via Make (if target is added):

```powershell
make openapi-spec
```

**Requirements:** `.env.local` must exist with minimal config (e.g. `SERVER_PORT`, `DATABASE_URL`) for the app to load. The script does not start the server; it only instantiates the app and exports the schema.

**Output:** `docs/openapi/openapi.json`

---

## 4. API Versioning

**[SPEC]**

**All routes are mounted under a `/v1` prefix.** `_register_v1_routers` (`server/app/factory.py`) builds
`APIRouter(prefix="/v1")` and mounts every router onto it, so every path in `openapi.json` begins with
`/v1`. Routers that additionally declare their own `/api` prefix therefore resolve under `/v1/api/...`.

Worked examples:

| Router surface | Effective path |
| --- | --- |
| Quest log | `GET /v1/api/players/{player_id}/quests` |
| Metrics | `GET /v1/metrics` (no `/api` segment) |
| Session replacement | `POST /v1/api/connections/{player_id}/session` |
| WebSocket | `/v1/api/ws` |

**[NOTE]**
This scheme was previously recorded in no design document, which caused several ADRs and FRDs to state
paths that would not resolve against the running server. When adding or citing an endpoint, take
`docs/openapi/openapi.json` as the authority for the effective path.

## 5. API Tag Organization

**[SPEC]**
Endpoints are grouped by tag in the specification:

| Tag | Description |
|-----|-------------|
| auth | JWT login, registration, user management |
| users | User account operations (FastAPI Users) |
| players | Player characters: create, list, select, delete, stats, effects |
| professions | Character class and profession data |
| game | Game state: enter game, movement, combat actions |
| containers | Unified container system: environmental, wearable, corpse storage |
| rooms | Room data and exploration |
| maps | ASCII map rendering and exploration views |
| realtime | WebSocket connection and real-time game events |
| monitoring | Health checks, performance metrics, observability |
| metrics | NATS and system metrics |
| admin | Administrative endpoints: NPC management, teleport |
| npc | NPC spawn and lifecycle administration |
| nats | NATS subject management (admin) |
| subjects | NATS subject inspection and management |
| system | System-level monitoring and diagnostics |

---

## 6. Service Interfaces (Internal)

**[SPEC]**
API routes call into **service layer** components. Service boundaries and contracts are documented in:

- **Bounded contexts:** [BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md](../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md)
- **Event ownership:** [EVENT_OWNERSHIP_MATRIX.md](../EVENT_OWNERSHIP_MATRIX.md)
- **Container API reference:** [CONTAINER_SYSTEM_API_REFERENCE.md](../CONTAINER_SYSTEM_API_REFERENCE.md)

The OpenAPI spec documents the **HTTP/WebSocket contracts** (request/response shapes, auth). Internal Python service interfaces are described in the bounded contexts document.

---

## 7. Using the Specification

**[SPEC]**

### 7.1 Client Generation

Use the OpenAPI spec to generate typed API clients:

```bash
# Example: openapi-generator (Java, TypeScript, Python, etc.)
npx @openapitools/openapi-generator-cli generate \
  -i docs/openapi/openapi.json \
  -g typescript-fetch \
  -o client/src/api/generated
```

### 7.2 Contract Testing

- Validate that the running server's `/openapi.json` matches the committed spec.
- Use tools like Dredd or Schemathesis for contract testing.

### 7.3 CI/CD

- Add a CI step to regenerate the spec and fail if it differs from the committed file (detects undocumented API changes).
- Or regenerate on each release and commit the updated spec.

---

## 8. Related Documentation

**[SPEC]**

| Document | Purpose |
|----------|---------|
| [BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md](../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md) | Service boundaries, bounded contexts, internal contracts |
| [CONTAINER_SYSTEM_API_REFERENCE.md](../CONTAINER_SYSTEM_API_REFERENCE.md) | Container endpoints, WebSocket events, examples |
| [EVENT_OWNERSHIP_MATRIX.md](../EVENT_OWNERSHIP_MATRIX.md) | Event flow, EventBus vs NATS, WebSocket delivery |
| [ADR-007-fastapi-async-await.md](decisions/ADR-007-fastapi-async-await.md) | FastAPI and async backend rationale |

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-19 | Record the /v1 versioning scheme; renumber sections |
