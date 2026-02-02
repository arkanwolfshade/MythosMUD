# ADR-004: WebSocket-Only Real-Time Architecture

**Status:** Accepted
**Date:** 2026-02-02

## Context

MythosMUD requires real-time bidirectional communication for gameplay: players send commands (move, attack, chat) and receive game state updates (room changes, combat events, chat messages). The architecture must support low latency, connection resilience, and straightforward client implementation. Multiple approaches exist: WebSocket, Server-Sent Events (SSE), long polling, or hybrid (e.g., REST + WebSocket).

## Decision

Use **WebSocket-only** for all real-time communication after initial REST authentication:

- **Authentication**: REST API with JWT tokens (e.g., `/api/auth/login`)
- **All game traffic**: Single WebSocket connection for commands and state updates
- **No SSE, no long polling** for game data

Clients establish one WebSocket connection per session. The connection carries both outbound commands (e.g., `say`, `move`, `attack`) and inbound events (e.g., `player_entered`, `combat_event`, `room_update`).

## Alternatives Considered

1. **REST + SSE** - Rejected: SSE is server-to-client only; would require separate connection for client-to-server commands (e.g., chat)
2. **REST + long polling** - Rejected: higher latency, more HTTP overhead, worse UX for real-time gameplay
3. **Dual WebSocket + SSE** - Rejected: adds complexity; WebSocket alone is sufficient for bidirectional needs
4. **GraphQL subscriptions** - Rejected: not adopted for this project; WebSocket is simpler and sufficient

## Consequences

- **Positive**: Single connection type reduces complexity; bidirectional over one channel; lower overhead than polling; mature, well-supported protocol
- **Negative**: WebSocket reconnection and state sync on reconnect require careful handling; no automatic HTTP retry semantics
- **Neutral**: ConnectionManager and RealTimeEventHandler manage WebSocket lifecycle; client must implement reconnection and backoff

## Related ADRs

- ADR-001: Layered Architecture with Event-Driven Components
- ADR-003: Dual Event Systems (EventBus + NATS)

## References

- [Real-Time Architecture](../../REAL_TIME_ARCHITECTURE.md)
- [Connection Manager Architecture](../../CONNECTION_MANAGER_ARCHITECTURE.md)
