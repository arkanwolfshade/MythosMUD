# Combat Taunt Tests

> 22 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (27 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_ensure_flee_standing()** (11 connections) — `server/commands/combat_flee.py`
- **test_validate_flee_combat_and_room_success()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_movement_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **.get_stats()** (3 connections) — `server/commands/combat_flee.py`
- **test_get_flee_player_uuid_accepts_uuid()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_get_flee_player_uuid_invalid_string()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_sitting()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_already_standing()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_combat_service()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **UUID** (2 connections)
- **Stats dict (position used for standing check).** (1 connections) — `server/commands/combat_flee.py`
- **If not standing, stand and return error message; else return None.** (1 connections) — `server/commands/combat_flee.py`
- **Unit tests for server.commands.combat_flee module-level helpers (not full /flee** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **UUID player_id passes through.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Bad UUID string returns error dict.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Non-standing returns scrabble message and optionally stands.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Standing player returns no error.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Without combat service, combat unavailable.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Combat resolved but movement missing.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Happy path returns combat and room_id.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`

## Relationships

- [Investigations Sessions Session](Investigations_Sessions_Session.md) (16 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (7 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (2 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (1 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (1 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (1 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 80 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*