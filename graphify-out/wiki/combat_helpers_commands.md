# combat helpers commands

> 37 nodes

## Key Concepts

- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (9 connections) — `server/commands/combat_loader.py`
- **_app_from_request()** (8 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (7 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (7 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (7 connections) — `server/commands/combat_loader.py`
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **handle_flee_command()** (6 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (6 connections) — `server/commands/combat_loader.py`
- **test_combat_helpers.py** (6 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **.combat_service()** (4 connections) — `server/commands/combat_handler.py`
- **test_format_combat_status_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_format_combat_status_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target_not_found()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Any** (2 connections)
- **Combat command handlers for the MUD.  This module re-exports combat command hand** (1 connections) — `server/commands/combat.py`
- **Combat service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Produce a human-readable combat status string.      This helper is retained for** (1 connections) — `server/commands/combat_helpers.py`
- **Resolve a combat target by name.      The current implementation is intentionall** (1 connections) — `server/commands/combat_helpers.py`
- **Combat command handler singleton and public async command entry points.  Extract** (1 connections) — `server/commands/combat_loader.py`
- **Get the global combat command handler instance, creating it if needed.     Uses** (1 connections) — `server/commands/combat_loader.py`
- *... and 12 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [combat commands handler](combat_commands_handler.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [combat flee commands](combat_flee_commands.md) (4 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [container helpers loot](container_helpers_loot.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [services combat sync](services_combat_sync.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_helpers.py`

## Audit Trail

- EXTRACTED: 150 (90%)
- INFERRED: 17 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*