# asyncio

> 25 nodes

## Key Concepts

- **asyncio** (18 connections)
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **test_publish_combat_started_nats_error()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_no_nats_service()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_legacy_subject_without_manager()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_player_attacked_no_nats_service()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_not_connected()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_turn_advanced_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_died_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_took_damage_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_player_attacked_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **.publish_combat_started_event()** (3 connections) — `server/services/combat_service.py`
- **Event fired when combat begins.** (1 connections) — `server/events/combat_events.py`
- **Publish a combat started event to NATS.** (1 connections) — `server/services/combat_service.py`
- **Test publish_combat_started() when NATS service is None.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_started() handles NATS publish error.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_player_attacked() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_npc_took_damage() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_npc_died() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_turn_advanced() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_player_attacked() when NATS service is None.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Legacy subject construction when subject_manager is absent.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_started() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_started() when NATS is not connected.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`

## Relationships

- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (14 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [combat_event_publisher.py](combat_event_publisher.py.md) (4 shared connections)
- [CombatEventPublisher](CombatEventPublisher.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [CombatEndedEvent](CombatEndedEvent.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [NATSPublishError](NATSPublishError.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 48 (74%)
- INFERRED: 17 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*