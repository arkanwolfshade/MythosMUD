# nats exceptions services

> 81 nodes

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
- **.test_connection_error_with_original_error()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- *... and 56 more nodes in this community*

## Relationships

- [message filtering realtime](message_filtering_realtime.md) (20 shared connections)
- [combat validator validators](combat_validator_validators.md) (11 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (9 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (8 shared connections)
- [nats services service](nats_services_service.md) (7 shared connections)
- [alias command models](alias_command_models.md) (6 shared connections)
- [motd loader rationale](motd_loader_rationale.md) (5 shared connections)
- [nats message handler](nats_message_handler.md) (4 shared connections)
- [services combat sync](services_combat_sync.md) (2 shared connections)
- [combat commands handler](combat_commands_handler.md) (1 shared connections)
- [persistence combat handler](persistence_combat_handler.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 273 (78%)
- INFERRED: 75 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*