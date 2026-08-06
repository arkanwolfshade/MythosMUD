# commands communication say

> 83 nodes

## Key Concepts

- **nats_exceptions.py** (36 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (35 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSError** (9 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (7 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- **.test_connection_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_publish_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_subscribe_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_health_check_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_exception_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **test_subscribe_to_subject_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **.test_nats_error_creation()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_nats_error_inheritance()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_with_url()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- *... and 58 more nodes in this community*

## Relationships

- [game chat service](game_chat_service.md) (23 shared connections)
- [combat commands handler](combat_commands_handler.md) (7 shared connections)
- [alias command models](alias_command_models.md) (6 shared connections)
- [follow game service](follow_game_service.md) (6 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (6 shared connections)
- [commands inventory put](commands_inventory_put.md) (5 shared connections)
- [combat validator validators](combat_validator_validators.md) (5 shared connections)
- [subject admin controller](subject_admin_controller.md) (4 shared connections)
- [nats message handler](nats_message_handler.md) (4 shared connections)
- [target resolution service](target_resolution_service.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [connection state machine](connection_state_machine.md) (3 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 278 (79%)
- INFERRED: 75 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*