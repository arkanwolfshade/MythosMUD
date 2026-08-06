# payload realtime optimizer

> 10 nodes

## Key Concepts

- **MythosValidationError** (10 connections)
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_process_command_string_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_apply_combat_effects_validation_error()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **Test process_validated_command handles ValidationError.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _parse_command_string handles ValidationError.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _create_command_object re-raises MythosValidationError without wrapping.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test process_command_string handles MythosMUD validation errors.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`

## Relationships

- [add used user](add_used_user.md) (3 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (2 shared connections)
- [health service services](health_service_services.md) (2 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (1 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [command communication models](command_communication_models.md) (1 shared connections)
- [services nats service](services_nats_service.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [command processor rationale](command_processor_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 19 (59%)
- INFERRED: 13 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*