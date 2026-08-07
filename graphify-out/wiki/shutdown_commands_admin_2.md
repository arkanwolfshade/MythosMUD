# shutdown commands admin

> 55 nodes

## Key Concepts

- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (22 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **_app_from_request()** (11 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (11 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **test_combat_helpers.py** (6 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **.combat_service()** (4 connections) — `server/commands/combat_handler.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **test_format_combat_status_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_format_combat_status_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target_not_found()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_command_handler_creates_singleton()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_attack_command_delegates()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_punch_command_sets_type()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- *... and 30 more nodes in this community*

## Relationships

- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (11 shared connections)
- [commands npc admin](commands_npc_admin.md) (8 shared connections)
- [combat flee commands](combat_flee_commands.md) (4 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [container helpers loot](container_helpers_loot.md) (2 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [character creation service](character_creation_service.md) (1 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_helpers.py`
- `server/tests/unit/commands/test_combat_loader.py`

## Audit Trail

- EXTRACTED: 234 (92%)
- INFERRED: 19 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*