# NATSError

> 77 nodes

## Key Concepts

- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **test_nats_message_handler_subzone_events.py** (36 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **asyncio** (24 connections)
- **TestNATSError** (5 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **test_cleanup_empty_subzone_subscriptions_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_exception()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_subscribe_to_event_subjects_partial_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_subscribe_to_subzone_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_cleanup_empty_subzone_subscriptions()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_combat_ended_event()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_combat_started_event()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_event_message()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_npc_attacked_event()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_npc_died_event()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_npc_took_damage_event()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_attacked_event()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_different_subzone()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_new_subzone_none()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_old_subzone_none()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_same_subzone()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_subscribe_to_subzone_no_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_subscribe_to_subzone_subscribe_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_event_subjects_partial()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- *... and 52 more nodes in this community*

## Relationships

- [nats_exceptions.py](nats_exceptions.py.md) (14 shared connections)
- [CombatService](CombatService.md) (10 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (9 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [models/combat.py](models-combat.py.md) (3 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [CombatPersistenceHandler](CombatPersistenceHandler.md) (2 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (2 shared connections)
- [test_combat_persistence_handler_events.py](test_combat_persistence_handler_events.py.md) (2 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 132 (79%)
- INFERRED: 36 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*