# Distributed EventBus via NATS

**Version 1.0.0** · MythosMUD · 2026-07-30

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
**Status:** Implemented
**Purpose:** Document the NATS-backed distributed EventBus for horizontal scaling.

---

## 2. Overview

**[SPEC]**
The EventBus is now distributed across server instances using NATS. When any instance publishes a domain event, all instances (including the publisher) receive it, enabling horizontal scaling without Redis.

### 1.1 Components

| Component | Purpose |
|-----------|---------|
| `DistributedEventBus` | Wraps local EventBus; publishes to NATS when configured |
| `NATSEventBusBridge` | Serializes events, publishes to NATS, subscribes and injects received events |
| `event_serialization` | Serialize/deserialize BaseEvent to/from JSON-compatible dicts |
| `EventBus.inject()` | Inject event from remote source without re-publishing to NATS |

### 1.2 Subject Pattern

Domain events are published to:

```
events.domain.{EventType}
```

Examples: `events.domain.PlayerEnteredRoom`, `events.domain.PlayerDiedEvent`

All instances subscribe to `events.domain.>` (wildcard) to receive every domain event.

---

## 3. Flow

**[SPEC]**

### Local Publish

1. Domain code calls `event_bus.publish(event)`
2. DistributedEventBus delegates to parent EventBus (local delivery)
3. DistributedEventBus schedules `nats_bridge.publish(event)` (fire-and-forget)
4. Bridge serializes event and publishes to NATS `events.domain.{EventType}`

### Remote Receive

1. NATS delivers message to subscriber on `events.domain.>`
2. Bridge deserializes dict to BaseEvent
3. Bridge calls `event_bus.inject(event)` (no NATS re-publish)
4. EventBus queues event and dispatches to local subscribers

---

## 4. Configuration

**[SPEC]**

- **NATS enabled:** Bridge starts when RealtimeBundle initializes and NATS connects
- **NATS disabled:** EventBus behaves as single-instance (no NATS publish/subscribe)

---

## 5. Related

**[SPEC]**

- [ADR-003: Dual Event Systems (EventBus + NATS)](decisions/ADR-003-dual-event-systems-eventbus-nats.md)
- [EVENT_OWNERSHIP_MATRIX](../EVENT_OWNERSHIP_MATRIX.md)
- [NATS_SUBJECT_PATTERNS](../NATS_SUBJECT_PATTERNS.md)
- [Architecture Review Plan](../../.cursor/plans/architecture_review_plan_7bcbc812.plan.md) – evaluate-distributed-eventbus

## 6. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
