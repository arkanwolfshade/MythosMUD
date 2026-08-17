# combat_event_publisher.py

> 12 nodes

## Key Concepts

- **combat_event_publisher.py** (23 connections) — `server/services/combat_event_publisher.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **CombatTimeoutEvent** (8 connections) — `server/events/combat_events.py`
- **CombatTurnAdvancedEvent** (8 connections) — `server/events/combat_events.py`
- **test_publish_combat_timeout_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_attacked_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Event fired when combat times out.** (1 connections) — `server/events/combat_events.py`
- **Event fired when an NPC is attacked.** (1 connections) — `server/events/combat_events.py`
- **Event fired when combat turn advances.** (1 connections) — `server/events/combat_events.py`
- **Combat event publisher for MythosMUD. This module provides a service for…** (1 connections) — `server/services/combat_event_publisher.py`
- **Test publish_npc_attacked() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_timeout() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (9 shared connections)
- [CombatEventPublisher](CombatEventPublisher.md) (5 shared connections)
- [asyncio](asyncio.md) (4 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (1 shared connections)
- [CombatEndedEvent](CombatEndedEvent.md) (1 shared connections)
- [NATSPublishError](NATSPublishError.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_event_publisher.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 43 (81%)
- INFERRED: 10 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*