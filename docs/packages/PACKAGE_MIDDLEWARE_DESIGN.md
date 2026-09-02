# Middleware Package Design

**Version 1.0.0** · MythosMUD · 2026-08-29

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`server/middleware/` is the request-pipeline layer every HTTP and WebSocket request passes
through before reaching a route handler: security headers, correlation IDs, auth-endpoint rate
limiting, per-player command rate limiting, structured request/response logging, and centralized
exception handling. This document is reverse-engineered from code; code is the source of truth
(see [`docs/subsystems/README.md`](../subsystems/README.md) for the same posture applied to
behavioral subsystems). Written to close [`#740`](https://github.com/arkanwolfshade/MythosMUD/issues/740).

## 2. Members

**[SPEC]**

| Cluster | Files | Purpose |
| --- | --- | --- |
| HTTP request pipeline | `security_headers.py`, `auth_rate_limit.py`, `comprehensive_logging.py`, `error_handling_middleware.py` | Pure-ASGI middleware wrapped around every HTTP request via `app.add_middleware` in [`server/app/factory.py`](../../server/app/factory.py). |
| HTTP correlation | `correlation_middleware.py` | `CorrelationMiddleware` — attaches a request-scoped correlation ID to every HTTP request for cross-log tracing. Wired into the app in `server/main.py`. WebSocket connections get their correlation context bound directly in the WS handler (`server/realtime/websocket_handler.py`, `websocket_handler_message_loop.py`) rather than via middleware — Starlette has no per-connection middleware hook to attach one through, so a former `WebSocketCorrelationMiddleware` in this module (never wired in, `#754`) was deleted rather than fixed. |
| Command-level rate limiting | `command_rate_limiter.py` | `CommandRateLimiter`, a sliding-window limiter keyed by player name. Not ASGI middleware — a plain class instantiated once as a module-level singleton (`command_rate_limiter`) and called directly from [`server/command_handler_unified.py:215`](../../server/command_handler_unified.py). |
| Metrics | `metrics_collector.py` | `MetricsCollector` — in-memory counters for NATS message delivery (processed/failed/retried/DLQ/circuit-breaker state). Not ASGI middleware; instantiated and used by [`server/realtime/nats_message_handler_base.py`](../../server/realtime/nats_message_handler_base.py). Naming is the one real drift in this package: it lives beside four ASGI middleware modules but has nothing to do with the request pipeline. |
| Package surface | `__init__.py` | Re-exports only the error-handling entry points (`ErrorHandlingMiddleware`, `add_error_handling_middleware`, `register_error_handlers`, `setup_error_handling`). Every other member is imported by its own module path, not via the package `__init__`. |

## 3. Boundary contract

**[SPEC]**

**Exports.** No single facade — callers import each middleware class or function directly from
its module. The only re-exports are the error-handling four in `__init__.py`.

**Dependents.**

- `server/app/factory.py` — wires `SecurityHeadersMiddleware`, `AuthRateLimitMiddleware`,
  `ComprehensiveLoggingMiddleware`, and (via `setup_error_handling`) `ErrorHandlingMiddleware`
  into `create_app()`; also calls `assert_auth_rate_limit_paths_registered(app)` as a startup
  invariant check (§4).
- `server/main.py` — adds `CorrelationMiddleware` after `create_app()` returns, making it the
  outermost wrapper of all (see request-flow diagram below).
- `server/command_handler_unified.py` — calls the `command_rate_limiter` singleton directly,
  not via `app.add_middleware`.
- `server/realtime/nats_message_handler_base.py` — instantiates `MetricsCollector` directly.

**Invariants a caller must not violate:**

- **Registration order is load-bearing, not incidental.** `factory.py:310-311` states it in a
  comment: *"Starlette last-added is outermost. `AuthRateLimit` must sit inside logging so 429s
  still pass through `send_with_logging`"* — i.e. rate-limit rejections must still be
  observable in access logs. Request flow, outermost to innermost:

  ```mermaid
  flowchart LR
    Req[Incoming request] --> Correlation[CorrelationMiddleware<br/>main.py, added last]
    Correlation --> ErrorHandling[ErrorHandlingMiddleware]
    ErrorHandling --> CORS[CORSMiddleware]
    CORS --> Logging[ComprehensiveLoggingMiddleware]
    Logging --> AuthLimit[AuthRateLimitMiddleware]
    AuthLimit --> SecHeaders[SecurityHeadersMiddleware<br/>factory.py, added first]
    SecHeaders --> Route[Route handler]
  ```

  Reordering any `add_middleware` call changes which layers see a request that a lower layer
  rejects — moving `AuthRateLimitMiddleware` outside `ComprehensiveLoggingMiddleware` would
  silently drop 429s from access-log telemetry.
- **`AUTH_RATE_LIMITED_PATHS` must match the mounted route table.** `assert_auth_rate_limit_paths_registered` (`auth_rate_limit.py:104`) fails startup if the hardcoded path
  set drifts from what is actually mounted — a new auth POST route that forgets to update the
  frozenset is caught at boot, not silently unprotected.
  `is_auth_rate_limited_path` is the single source of truth `AuthRateLimitMiddleware.__call__`
  consults per-request.
- **Pure ASGI, not `BaseHTTPMiddleware`**, for four of the five HTTP middleware classes —
  `security_headers.py:12-13` and `error_handling_middleware.py` both note this is a deliberate
  performance/type-safety choice, not an oversight. Each still exposes a `dispatch()` method for
  `BaseHTTPMiddleware`-style test/compat callers.
- **`command_rate_limiter` and `MetricsCollector` are plain singletons, not part of the ASGI
  chain** — do not `app.add_middleware()` them; call their methods directly.

## 4. Key design decisions

**[SPEC]**

- **Rate limiting is split two ways, at two different layers.** `AuthRateLimitMiddleware` gates
  unauthenticated auth POSTs (login/register) at the ASGI layer, keyed by client IP
  (`auth_client_key`). `CommandRateLimiter` gates in-game commands post-authentication, keyed by
  player name, called directly from the command dispatcher rather than as middleware — the two
  never share a code path, by design (different identity, different point of enforcement).
- **`setup_error_handling` composes two registrations, not one.** It calls both
  `add_error_handling_middleware` (the ASGI exception-catching layer) and
  `register_error_handlers` (FastAPI's typed exception handlers for `MythosMUDError`,
  `ValidationError`, `HTTPException`, `LoggedHTTPException`, and the generic fallback). Both
  independently-callable functions exist so a caller could use one without the other; production
  (`factory.py:333`) always uses the composed form.
- **`include_details` is environment-gated**, not a hardcoded constant: `factory.py:329` computes
  it from `ENV != "production"`, so error responses carry stack detail in development and are
  scrubbed in production. This is the same env-driven pattern documented for
  `SECURITY_ENVIRONMENT_VARIABLES.md`.

## 5. Constraints

**[SPEC]**

- Every ASGI middleware class implements `__call__(self, scope, receive, send)`, not `dispatch`,
  as the primary interface; `dispatch()` exists only for `BaseHTTPMiddleware`-style callers
  (tests, or any future integration expecting that interface).
- `CommandRateLimiter.is_allowed` / `get_wait_time` assume a monotonic-ish `now_provider`;
  the default is `datetime.now`, injectable for tests.
- `assert_auth_rate_limit_paths_registered` must run after all routers are registered
  (`factory.py` calls it as the last line of `create_app()`, after `_register_v1_routers`) — an
  earlier call would false-positive on paths not yet mounted.

## 6. Developer guide

**[NOTE]**

- **Adding a new unauthenticated auth POST route**: add its path to `AUTH_RATE_LIMITED_PATHS` in
  `auth_rate_limit.py`, or `assert_auth_rate_limit_paths_registered` fails startup.
- **Adding new ASGI middleware to the HTTP pipeline**: decide where it sits relative to
  `ComprehensiveLoggingMiddleware` and `AuthRateLimitMiddleware` explicitly — see the ordering
  invariant in §3 — and add the reasoning as a comment in `factory.py`, matching the existing
  one.
- **Tests**: `server/tests/unit/middleware/` — one file per module, mirroring the source layout.

## 7. Troubleshooting

**[NOTE]**

- **429s missing from access logs**: check middleware registration order in `factory.py` —
  `AuthRateLimitMiddleware` must be added before (i.e. sit inside) `ComprehensiveLoggingMiddleware`.
- **Startup fails with an `assert_auth_rate_limit_paths_registered` error**: a mounted POST auth
  route isn't in `AUTH_RATE_LIMITED_PATHS`, or the reverse — the set names a path that isn't
  actually mounted. Reconcile the two.
- **Command rate limiting not applying**: confirm the caller imports the module-level
  `command_rate_limiter` singleton, not the `CommandRateLimiter` class — instantiating a second
  limiter creates independent state.

## 8. Related docs

**[SPEC]**

- [`docs/subsystems/README.md`](../subsystems/README.md) — the sibling reverse-engineered-doc
  family, behavioral rather than structural axis.
- [`SECURITY_ENVIRONMENT_VARIABLES.md`](../SECURITY_ENVIRONMENT_VARIABLES.md) — env-driven
  security configuration, same pattern `include_details` follows.
- [`API_OPENAPI_SPECIFICATION.md`](../architecture/API_OPENAPI_SPECIFICATION.md) — the routes
  this pipeline wraps.

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-29 | Initial version, closes #740 |
