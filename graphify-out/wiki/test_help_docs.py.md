# test_help_docs.py

> 84 nodes · cohesion 0.04

## Key Concepts

- **CombatCommandHandler** (57 connections) — `server/commands/combat_handler.py`
- **test_flee_command.py** (28 connections) — `server/tests/unit/commands/test_flee_command.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_request_with_persistence()** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_no_exits_returns_no_escape()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_fails_returns_failure_and_uses_action()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_succeeds_returns_success()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **.get_player_and_room()** (7 connections) — `server/commands/combat_handler.py`
- **._get_persistence_from_app()** (6 connections) — `server/commands/combat_handler.py`
- **Any** (6 connections)
- **handler()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_make_participant()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_standing_player_id()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_in_combat_returns_message()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_standing_forces_stand_and_returns_message()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_get_combat_command_handler_includes_flee()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **.handle_assist_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_protect_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **asyncio** (5 connections)
- **.combat_service()** (4 connections) — `server/commands/combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.get_npc_instance()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- *... and 59 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (18 shared connections)
- [test_command_parser_helpers.py](test_command_parser_helpers.py.md) (4 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (4 shared connections)
- [ChatLogger](ChatLogger.md) (4 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (4 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (4 shared connections)
- [CommandFactory](CommandFactory.md) (3 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (2 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`

## Audit Trail

- EXTRACTED: 165 (85%)
- INFERRED: 28 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*