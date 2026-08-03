# shutdown command commands

> 10 nodes

## Key Concepts

- **player_repository_room.py** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room_with_persistence()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **should_skip_room_validation()** (5 connections) — `server/persistence/repositories/player_repository_room.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **Player room validation helpers for PlayerRepository.  Validates and fixes invali** (1 connections) — `server/persistence/repositories/player_repository_room.py`
- **Return True if room validation should be skipped (cache empty, instanced, or tut** (1 connections) — `server/persistence/repositories/player_repository_room.py`
- **Validate player's current room and fix if invalid.      Args:         room_cache** (1 connections) — `server/persistence/repositories/player_repository_room.py`
- **Validate and fix player room, persisting the fix if needed.      Args:         r** (1 connections) — `server/persistence/repositories/player_repository_room.py`

## Relationships

- [Database Config](Database_Config.md) (4 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository_room.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*