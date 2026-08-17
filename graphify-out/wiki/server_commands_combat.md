# server commands combat

> 53 nodes

## Key Concepts

- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (23 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **_app_from_request()** (12 connections) — `server/commands/combat_loader.py`
- **CombatCommandHandlerExtras** (9 connections) — `server/commands/combat_handler.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **test_combat_helpers.py** (6 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **asyncio** (6 connections)
- **test_handle_attack_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_flee_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_kick_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_punch_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_strike_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_taunt_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_format_combat_status_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_format_combat_status_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- *... and 28 more nodes in this community*

## Relationships

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (8 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (5 shared connections)
- [server commands combat flee](server_commands_combat_flee.md) (4 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (4 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (2 shared connections)
- [eventbus](eventbus.md) (1 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)
- [playercombatservice](playercombatservice.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_helpers.py`
- `server/tests/unit/commands/test_combat_loader.py`

## Audit Trail

- EXTRACTED: 129 (83%)
- INFERRED: 26 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*