# asyncio

> 21 nodes

## Key Concepts

- **asyncio** (18 connections)
- **test_publish_combat_started_nats_error()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_no_nats_service()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_legacy_subject_without_manager()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_player_attacked_no_nats_service()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_not_connected()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_attacked_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_died_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_took_damage_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_player_attacked_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_started() when NATS service is None.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_started() handles NATS publish error.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_player_attacked() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_npc_attacked() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_npc_took_damage() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_npc_died() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_player_attacked() when NATS service is None.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Legacy subject construction when subject_manager is absent.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_started() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_started() when NATS is not connected.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`

## Relationships

- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (13 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (10 shared connections)
- [CombatEventPublisher](CombatEventPublisher.md) (3 shared connections)
- [CombatEndedEvent](CombatEndedEvent.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [CombatTimeoutEvent](CombatTimeoutEvent.md) (1 shared connections)
- [CombatTurnAdvancedEvent](CombatTurnAdvancedEvent.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 38 (73%)
- INFERRED: 14 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*