# Investigations Sessions Session

> 13 nodes

## Key Concepts

- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **_resolve_flee_preconditions()** (15 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **_PlayerForFlee** (11 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **run_handle_flee_command()** (6 connections) — `server/commands/combat_flee.py`
- **UUID** (4 connections)
- **Flee command flow: preconditions and execution.  Extracted from combat.py to red** (1 connections) — `server/commands/combat_flee.py`
- **Player attributes used by flee preconditions.** (1 connections) — `server/commands/combat_flee.py`
- **Resolve player_id to UUID; return (uuid, None) or (None, error_dict).** (1 connections) — `server/commands/combat_flee.py`
- **Resolve combat, room, exits, and movement service for flee.     Returns (combat,** (1 connections) — `server/commands/combat_flee.py`
- **Resolve player, player_id, combat, and room_id for flee.     Returns (player, pl** (1 connections) — `server/commands/combat_flee.py`
- **Handle /flee command: leave combat and move to random adjacent room.     Standin** (1 connections) — `server/commands/combat_flee.py`

## Relationships

- [Combat Taunt Tests](Combat_Taunt_Tests.md) (13 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (7 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (7 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (5 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (4 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`

## Audit Trail

- EXTRACTED: 81 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*