# game chat service

> 164 nodes

## Key Concepts

- **NATSError** (105 connections) — `server/services/nats_exceptions.py`
- **test_nats_message_handler_subzone_events.py** (36 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **test_combat_persistence_handler.py** (14 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (6 connections) — `server/services/combat_persistence_handler.py`
- **.publish_combat_ended_event()** (5 connections) — `server/services/combat_event_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **Any** (3 connections)
- **test_unsubscribe_from_subzone_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_exception()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_subscribe_to_subzone_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_subscribe_to_event_subjects_partial_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_cleanup_empty_subzone_subscriptions_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **persistence_handler()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- *... and 139 more nodes in this community*

## Relationships

- [commands communication say](commands_communication_say.md) (23 shared connections)
- [follow game service](follow_game_service.md) (13 shared connections)
- [subject admin controller](subject_admin_controller.md) (11 shared connections)
- [models npc rationale](models_npc_rationale.md) (9 shared connections)
- [tick game processing](tick_game_processing.md) (9 shared connections)
- [nats message handler](nats_message_handler.md) (9 shared connections)
- [profession models rationale](profession_models_rationale.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [message queue realtime](message_queue_realtime.md) (3 shared connections)
- [EdgeCreationModal map STANDARD](EdgeCreationModal_map_STANDARD.md) (3 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)

## Source Files

- `server/services/combat_event_handler.py`
- `server/services/combat_persistence_handler.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 436 (88%)
- INFERRED: 59 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*