# command parser rationale

> 86 nodes

## Key Concepts

- **test_command_parser.py** (45 connections) — `server/tests/unit/utils/test_command_parser.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **test_command_parser_smoke.py** (8 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_basic()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_args()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_pipes()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **command_parser()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_empty_string()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_whitespace_only()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_too_long()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_valid_look()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_valid_go()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_with_slash_prefix()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_spawn_alias()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_alias_l()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_alias_g()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_global_function()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_global_function_with_args()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_command_parser_initialization()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_normalize_command_removes_slash()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_normalize_command_cleans_whitespace()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_normalize_command_no_slash()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_parts_basic()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- *... and 61 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (3 shared connections)
- [command factories create](command_factories_create.md) (3 shared connections)
- [command processor rationale](command_processor_rationale.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [health service services](health_service_services.md) (1 shared connections)
- [commands position system](commands_position_system.md) (1 shared connections)
- [combat services initialization](combat_services_initialization.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_command_parser_smoke.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 217 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*