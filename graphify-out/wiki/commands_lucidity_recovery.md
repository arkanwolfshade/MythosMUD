# commands lucidity recovery

> 38 nodes

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
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **test_get_combat_command_handler_creates_singleton()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_attack_command_delegates()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_punch_command_sets_type()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_kick_command_sets_type()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_strike_command_sets_type()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_flee_command_delegates()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_taunt_command_delegates()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_get_combat_command_handler_requires_app()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_app_from_request_none()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_app_from_request_returns_app()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **Combat command handlers for the MUD.  This module re-exports combat command hand** (1 connections) — `server/commands/combat.py`
- *... and 13 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (14 shared connections)
- [commands party examples](commands_party_examples.md) (7 shared connections)
- [combat flee commands](combat_flee_commands.md) (5 shared connections)
- [container helpers loot](container_helpers_loot.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_loader.py`

## Audit Trail

- EXTRACTED: 199 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*