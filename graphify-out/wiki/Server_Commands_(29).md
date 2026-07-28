# Server Commands (29)

> 41 nodes

## Key Concepts

- **combat.py** (19 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (9 connections) — `server/commands/combat_loader.py`
- **_app_from_request()** (8 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (8 connections) — `server/commands/combat_loader.py`
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **handle_flee_command()** (6 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (6 connections) — `server/commands/combat_loader.py`
- **test_combat_helpers.py** (6 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **.combat_service()** (4 connections) — `server/commands/combat_handler.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **test_format_combat_status_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_format_combat_status_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target_not_found()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Any** (2 connections)
- **Combat command handlers for the MUD.  This module re-exports combat command hand** (1 connections) — `server/commands/combat.py`
- **Combat service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Movement service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Player position service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- *... and 16 more nodes in this community*

## Relationships

- [Server Services (6)](Server_Services_%286%29.md) (10 shared connections)
- [Server Commands](Server_Commands.md) (10 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (8 shared connections)
- [Server Commands (20)](Server_Commands_%2820%29.md) (4 shared connections)
- [Server Commands (37)](Server_Commands_%2837%29.md) (2 shared connections)
- [Server Game](Server_Game.md) (2 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (1 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (1 shared connections)
- [Server App](Server_App.md) (1 shared connections)
- [Server Realtime (44)](Server_Realtime_%2844%29.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_helpers.py`

## Audit Trail

- EXTRACTED: 133 (84%)
- INFERRED: 25 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*