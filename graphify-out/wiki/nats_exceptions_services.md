# nats exceptions services

> 91 nodes

## Key Concepts

- **NATSPublishError** (35 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSError** (9 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (7 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **Exception** (6 connections)
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **.test_connection_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_publish_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_subscribe_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_health_check_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_exception_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- *... and 66 more nodes in this community*

## Relationships

- [commands communication say](commands_communication_say.md) (21 shared connections)
- [combat validator validators](combat_validator_validators.md) (12 shared connections)
- [combat commands handler](combat_commands_handler.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [alias command models](alias_command_models.md) (4 shared connections)
- [nats message handler](nats_message_handler.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 276 (77%)
- INFERRED: 81 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*