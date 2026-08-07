# game chat service

> 199 nodes

## Key Concepts

- **NATSError** (105 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **test_combat_persistence_handler.py** (14 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSError** (9 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (7 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (6 connections) — `server/services/combat_persistence_handler.py`
- **Exception** (6 connections)
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- *... and 174 more nodes in this community*

## Relationships

- [Memory Task Runtime](Memory_Task_Runtime.md) (36 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (14 shared connections)
- [nats message handler](nats_message_handler.md) (12 shared connections)
- [command parser helpers](command_parser_helpers.md) (10 shared connections)
- [combat helpers commands](combat_helpers_commands.md) (7 shared connections)
- [message nats handler](message_nats_handler.md) (6 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (4 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (4 shared connections)
- [subject admin controller](subject_admin_controller.md) (4 shared connections)
- [combat validator validators](combat_validator_validators.md) (4 shared connections)
- [message queue realtime](message_queue_realtime.md) (3 shared connections)
- [services service phantom](services_service_phantom.md) (3 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/services/combat_persistence_handler.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 573 (82%)
- INFERRED: 125 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*