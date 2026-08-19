# ADR-020: WebSocket Authentication and CSRF

**Version 1.0.0** · MythosMUD · 2026-08-19

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-08-19

This addendum to [ADR-004](ADR-004-websocket-only-realtime.md) records how MythosMUD
authenticates WebSockets, binds path `player_id` to the JWT subject, requires CSRF
on every realtime message, and rate-limits unauthenticated auth HTTP POSTs.
It closes GHSA-pc52-rx52-9jwc.

## 2. Context

**[NOTE]**
Realtime traffic is WebSocket-only. The handshake JWT is stored as connection
`token` and must be echoed as `csrfToken` on subsequent messages. Anonymous
`player_id` query fallback was a test convenience and a production hole.

**[BUG]**
GHSA-pc52-rx52-9jwc: CSRF fail-open, optional JWT on `/ws/{player_id}`, anonymous
player_id query, and missing auth-endpoint rate limits.

## 3. Decision

**[SPEC]**

- `/ws/{player_id}` requires a JWT. The path UUID is an identity check against the
  token's player, not a credential.
- CSRF validation is fail-closed: missing message token or missing expected token
  is `csrf_token_missing`. The production client always sends `csrfToken`
  (`useWebSocketConnection`).
- Anonymous `player_id` query fallback is off unless
  `MYTHOSMUD_ALLOW_WEBSOCKET_PLAYER_ID_FALLBACK` is in `{1,true,yes,on}`. Never
  enable in production.
- Unauthenticated POST `/v1/auth/login`, `/v1/auth/jwt/login`, and
  `/v1/auth/register` are IP-rate-limited (10/min). Startup asserts those paths
  exist as POST routes. Keys use the TCP peer unless
  `MYTHOSMUD_TRUST_X_FORWARDED_FOR` is set behind a proxy that overwrites
  `X-Forwarded-For`.
- Auth rate-limit middleware sits inside comprehensive logging (Starlette last-added
  is outermost) so 429s are logged.
- `server.api.real_time` loads `websocket_handler` and connection-manager lookup
  via importlib to avoid an import cycle with `app.factory`.

## 4. Alternatives Considered

**[SPEC]**

1. **CSRF fail-open when expected token is missing** - Rejected: GHSA finding.
2. **Treat path UUID as authentication** - Rejected: UUID is not a secret.
3. **Always trust `X-Forwarded-For`** - Rejected: spoofable without a trusted proxy.
4. **Static import of `websocket_handler` from `real_time`** - Rejected:
   `reportImportCycles` with `app.factory`.

## 5. Consequences

**[SPEC]**

- Positive: handshake and messages share one JWT; brute-force logins are limited
  and visible in request logs.
- Negative: clients that omit `csrfToken` are disconnected; tests and harnesses
  must send CSRF.
- Neutral: no database schema change; env flags default off.
