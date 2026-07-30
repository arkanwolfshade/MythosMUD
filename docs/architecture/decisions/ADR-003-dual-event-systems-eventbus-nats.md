# ADR-003: Dual Event Systems (EventBus + NATS)

**Version 1.0.0** · MythosMUD · 2026-07-30

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

## 2. Context

**[NOTE]**
MythosMUD needs two distinct event/messaging capabilities:

1. **In-process domain events** - When a player enters a room, combat starts, or an entity dies, multiple in-process subscribers (e.g., RealTimeEventHandler, logging) must react. Ordering and delivery are within a single process.
2. **Inter-process messaging** - Chat, combat broadcasts, and game ticks must reach multiple server instances or components that may run in separate processes. Messages must be durable, fan-out, and subject-based.

Using a single system for both would either over-complicate in-process events (e.g., NATS for every domain event) or under-serve distributed needs (e.g., EventBus cannot span processes).

## 3. Decision

**[SPEC]**
Maintain **two event systems** with clear separation of responsibility:

1. **EventBus** (`server/events/event_bus.py`) - In-memory pub/sub for domain events
   - Pure asyncio implementation
   - Events: PlayerEnteredRoom, CombatStartedEvent, PlayerDiedEvent, etc.
   - Subscribers: RealTimeEventHandler, logging, internal handlers
   - Single process only; no network

2. **NATS** (`server/services/nats_service.py`) - Distributed pub/sub for real-time messaging
   - Subject-based routing: `chat.say.{room_id}`, `combat.{room_id}`, `events.player_entered.{room_id}`
   - Used for: chat, combat broadcasts, cross-instance coordination
   - Supports horizontal scaling and multiple subscribers

Domain events flow: Domain → EventBus → RealTimeEventHandler → (optionally) NATS → WebSocket. Chat flows: ChatService → NATS → NATSMessageHandler → WebSocket.

## 4. Alternatives Considered

**[SPEC]**

1. **EventBus only** - Rejected: cannot scale horizontally; single-instance limitation
2. **NATS only** - Rejected: adds latency and complexity for in-process domain events; every domain event would require network round-trip
3. **Redis Pub/Sub instead of NATS** - Rejected at time of decision: NATS chosen for operational reasons (streaming, durability, subject hierarchy)
4. **Kafka** - Rejected: heavier operational footprint; NATS sufficient for current scale

## 5. Consequences

**[SPEC]**

- **Positive**: Clear separation of concerns; EventBus is fast for in-process events; NATS enables horizontal scaling for chat/combat
- **Negative**: Two systems to understand and operate; risk of event duplication if developers publish to both incorrectly (documented in EVENT_OWNERSHIP_MATRIX.md)
- **Neutral**: ~~EventBus is single-instance; horizontal scaling of game logic requires distributed EventBus (e.g., Redis) - deferred~~ **Implemented (2026-02):** Distributed EventBus via NATS. See DISTRIBUTED_EVENTBUS_NATS.md.

## 6. Related ADRs

**[SPEC]**

- ADR-001: Layered Architecture with Event-Driven Components
- ADR-004: WebSocket-Only Real-Time Architecture

## 7. References

**[SPEC]**

- [Event Ownership Matrix](../../EVENT_OWNERSHIP_MATRIX.md)
- [NATS Subject Patterns](../../NATS_SUBJECT_PATTERNS.md)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
