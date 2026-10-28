# QuestService

> 79 nodes · cohesion 0.04

## Key Concepts

- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **handle_command()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **test_command_aliases.py** (12 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_ensure_alias_storage()** (10 connections) — `server/command_handler_unified.py`
- **CommandRequest** (9 connections) — `server/command_handler_unified.py`
- **_run_expanded_alias()** (9 connections) — `server/command_handler_unified.py`
- **TestProcessAliasExpansion** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **process_command()** (7 connections) — `server/command_handler_unified.py`
- **asyncio** (7 connections)
- **TestHandleSpecialCommandRouting** (7 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **asyncio** (7 connections)
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (6 connections)
- **TestHandleCommand** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestProcessCommandUnified** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **_as_user_dict()** (5 connections) — `server/command_handler_unified.py`
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_handle_command_success()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_unauthorized()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_special_command_routing_alias_command()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_handle_special_command_routing_alias_command_no_storage()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- *... and 54 more nodes in this community*

## Relationships

- [test_movement_service.py](test_movement_service.py.md) (18 shared connections)
- [command_parser.py](command_parser.py.md) (13 shared connections)
- [look_container.py](look_container.py.md) (8 shared connections)
- [test_passive_corruption_flux_rate_overrides.py](test_passive_corruption_flux_rate_overrides.py.md) (5 shared connections)
- [go_command.py](go_command.py.md) (5 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (5 shared connections)
- [DialogueService](DialogueService.md) (5 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (4 shared connections)
- [mapUtils.ts](mapUtils.ts.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [CombatConfiguration](CombatConfiguration.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`

## Audit Trail

- EXTRACTED: 205 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*