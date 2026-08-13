# test_combat_flee_helpers.py

> 29 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (27 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **_get_flee_room_id()** (7 connections) — `server/commands/combat_flee.py`
- **test_validate_flee_combat_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **asyncio** (6 connections)
- **test_validate_flee_combat_and_room_no_movement_service()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_already_standing()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_sitting()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_resolve_flee_preconditions_player_error()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_combat_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_get_flee_player_uuid_accepts_uuid()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_get_flee_player_uuid_invalid_string()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_get_flee_room_id_no_exits()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_get_flee_room_id_unknown_room()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **UUID** (2 connections)
- **Ensure room exists and has exits; return (room_id, None) or (None, error_dict).** (1 connections) — `server/commands/combat_flee.py`
- **Resolve combat, room, exits, and movement service for flee. Returns (combat,…** (1 connections) — `server/commands/combat_flee.py`
- **Unit tests for server.commands.combat_flee module-level helpers (not full /flee…** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Combat resolved but movement missing.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **FleePreconditionError wraps get_player_and_room error.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Happy path returns combat and room_id.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **UUID player_id passes through.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Bad UUID string returns error dict.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Non-standing returns scrabble message and optionally stands.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- *... and 4 more nodes in this community*

## Relationships

- [combat_flee.py](combat_flee.py.md) (17 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [Player](Player.md) (2 shared connections)
- [combat_helpers.py](combat_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*