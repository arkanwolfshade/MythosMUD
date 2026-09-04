# ADR-004: WebSocket-Only Real-Time Architecture

**Version 1.1.0** · MythosMUD · 2026-08-28

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-02-02
**Provenance:** Post-hoc — authored after the systems it describes. See [README §2](README.md).

## 2. Context

**[NOTE]**
MythosMUD requires real-time bidirectional communication for gameplay: players send commands (move, attack, chat) and receive game state updates (room changes, combat events, chat messages). The architecture must support low latency, connection resilience, and straightforward client implementation. Multiple approaches exist: WebSocket, Server-Sent Events (SSE), long polling, or hybrid (e.g., REST + WebSocket).

## 3. Decision

**[SPEC]**
Use **WebSocket-only** for all real-time communication after initial REST authentication:

- **Authentication**: REST API with JWT tokens (e.g., `/api/auth/login`)
- **All game traffic**: Single WebSocket connection for commands and state updates
- **No SSE, no long polling** for game data

Clients establish a WebSocket connection per session.

> **Amended by [ADR-018](ADR-018-new-game-session-replacement.md) (2026-08-14).** The original
> one-connection-per-session claim no longer holds: registration **appends**, so
> `ConnectionManager.player_websockets` maps a player to a *list* of connections and a session may
> hold several (grace reconnect, multiple tabs). WebSocket-only transport is unaffected — only
> connection multiplicity changed.

The connection carries both outbound commands (e.g., `say`, `move`, `attack`) and inbound events (e.g., `player_entered`, `combat_event`, `room_update`).

## 4. Alternatives Considered

**[SPEC]**

1. **REST + SSE** - Rejected: SSE is server-to-client only; would require separate connection for client-to-server commands (e.g., chat)
2. **REST + long polling** - Rejected: higher latency, more HTTP overhead, worse UX for real-time gameplay
3. **Dual WebSocket + SSE** - Rejected: adds complexity; WebSocket alone is sufficient for bidirectional needs
4. **GraphQL subscriptions** - Rejected: not adopted for this project; WebSocket is simpler and sufficient

## 5. Consequences

**[SPEC]**

- **Positive**: Single connection type reduces complexity; bidirectional over one channel; lower overhead than polling; mature, well-supported protocol
- **Negative**: WebSocket reconnection and state sync on reconnect require careful handling; no automatic HTTP retry semantics
- **Neutral**: ConnectionManager and RealTimeEventHandler manage WebSocket lifecycle; client must implement reconnection and backoff

## 6. Related ADRs

**[SPEC]**

- ADR-001: Layered Architecture with Event-Driven Components
- ADR-003: Dual Event Systems (EventBus + NATS)

## 7. References

**[SPEC]**

- [Real-Time Architecture](../../REAL_TIME_ARCHITECTURE.md)
- [Connection Manager Architecture](../../CONNECTION_MANAGER_ARCHITECTURE.md)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-28 | Record provenance; cross-reference ADR-018's connection-multiplicity amendment (#721) |
