# test_combat_event_publisher.py

> 27 nodes

## Key Concepts

- **test_combat_event_publisher.py** (49 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_no_nats_service()** (9 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (9 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_attacked_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_died_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_took_damage_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_timeout_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_turn_advanced_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_player_attacked_event()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_ended_event()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_event_publisher_init()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_create_event_message()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_create_event_message_with_all_optional_fields()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_create_event_message_with_player_id()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_create_event_message_with_room_id()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_create_event_message_with_timestamp()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Unit tests for combat event publisher. Tests the CombatEventPublisher class.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test _create_event_message() includes room_id when provided.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test _create_event_message() includes player_id when provided.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test _create_event_message() uses provided timestamp.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test _create_event_message() includes all optional fields.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test CombatEventPublisher initialization.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Not-connected NATS returns False across remaining publish methods.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **None nats_service returns False for remaining publish methods.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- *... and 2 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (13 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (10 shared connections)
- [CombatEndedEvent](CombatEndedEvent.md) (5 shared connections)
- [CombatTimeoutEvent](CombatTimeoutEvent.md) (3 shared connections)
- [CombatTurnAdvancedEvent](CombatTurnAdvancedEvent.md) (3 shared connections)
- [combat_event_publisher](combat_event_publisher.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [CombatEventPublisher](CombatEventPublisher.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [test_combat_event_publisher_initialization_with_subject_manager](test_combat_event_publisher_initialization_with_subject_manager.md) (1 shared connections)
- [test_combat_event_publisher_initialization_with_nats_service](test_combat_event_publisher_initialization_with_nats_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 79 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*