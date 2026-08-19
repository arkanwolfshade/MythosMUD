# ADR-020: WebSocket Authentication and CSRF Model

**Version 1.0.0** · MythosMUD · 2026-08-19

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Proposed
**Date:** 2026-08-19
**Provenance:** Written contemporaneously with the decision, ahead of implementation. Status is
**Proposed** precisely because the model below is not yet in force — see §6. Do not read this ADR as a
description of current behaviour.

## 2. Context

**[NOTE]**
The 2026-08 design/implementation audit found that WebSocket authentication had no design record
anywhere in live documentation: a search for "csrf" across `docs/` returned matches only in
`docs/archive/`. `REAL_TIME_ARCHITECTURE.md` and `COMMAND_SECURITY_GUIDE.md` are both silent on it.

Issue #472 tracked a known CSRF validation gap. The main `/ws` path was subsequently hardened —
`resolve_expected_csrf_token` now sources an expected token from connection metadata rather than passing
`None`. That work is real. The gap survives through the paths described in §6.

## 3. Decision

**[SPEC]**
WebSocket connections authenticate by JWT, and message-level CSRF validation **fails closed**.

1. **Identity comes from the JWT only.** A connection is authenticated by a valid token carried on the
   WebSocket handshake. No other identity source is accepted in a production environment.

2. **Anonymous connection is a test-only affordance and must be explicitly enabled.** Any fallback that
   derives identity from a client-supplied `player_id` is gated behind an explicit configuration setting
   that is off by default and never enabled in production. Existence of a player record is **not**
   authentication.

3. **CSRF validation fails closed.** Once a connection carries a token, every message on it is validated.
   A connection with no expected token is not a licence to skip validation; the absence of a token is
   itself a rejectable state in production.

4. **One authenticated entry point.** `/v1/api/ws` is the supported route. Any compatibility route must
   perform the same authentication and pass the same token through to connection metadata, or be removed.

5. **Player identifiers are not secrets.** `player_id` values appear in event payloads delivered to other
   players, so no authentication or authorisation decision may rest on knowledge of a `player_id`.

## 4. Alternatives Considered

**[SPEC]**

1. **Keep the anonymous fallback for test convenience** — Rejected: the audit found no environment gate
   on it, so a test affordance was reachable in production. Test convenience is achieved with an explicit
   setting instead.
2. **Session cookies instead of JWT on the handshake** — Rejected: the client already carries a JWT and
   the REST surface already validates it; a second scheme adds surface without removing any.
3. **Leave CSRF validation permissive for backward compatibility** — Rejected: the backward-compatibility
   branch is what makes the gap reachable, and no supported client relies on it.

## 5. Consequences

**[SPEC]**

- **Positive**: a single authenticated entry point; no identity path that depends on a non-secret; CSRF
  behaviour that is safe by default rather than safe only when a token happens to be present.
- **Negative**: tests that relied on the implicit anonymous path must set the new flag explicitly; the
  compatibility route's consumers, if any, must migrate.
- **Neutral**: no change to transport (ADR-004) or to session replacement (ADR-018).

## 6. Current deviations from this decision

**[BUG]**
As of 2026-08-19 the implementation does **not** satisfy §3. Recorded here so the gap is visible in the
design record rather than only in an audit artifact:

1. `server/api/real_time.py` `_resolve_player_id` falls back to a `player_id` **query parameter** when the
   JWT is missing or invalid, and `_resolve_player_id_from_test` only checks that the player exists.
   The inline comment says "only for tests"; **no environment flag, config gate, or test-mode check
   enforces that.**
2. `server/realtime/message_validator.py` returns `True` when both the message token and the expected
   token are `None` ("backward compatibility"). Because path 1 produces a connection with no token, the
   auth bypass and the #472 CSRF gap are **the same hole**, not two.
3. A second route `/ws/{player_id}` is registered and marked deprecated. Whether it authenticates before
   trusting the path parameter was **not verified** by the audit and must be confirmed.

## 7. Related ADRs

**[SPEC]**

- [ADR-004: WebSocket-Only Real-Time Architecture](ADR-004-websocket-only-realtime.md)
- [ADR-018: New Game Session vs Grace Reconnect](ADR-018-new-game-session-replacement.md)
- [ADR-007: FastAPI with Async/Await](ADR-007-fastapi-async-await.md)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-19 | Initial ADR; records the intended model and the current deviations from it |
