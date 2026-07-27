# Persistence Repositories Player

> 10 nodes · cohesion 0.33

## Key Concepts

- **validate_and_fix_player_room()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room_with_persistence()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **player_repository_room.py** (5 connections) — `server/persistence/repositories/player_repository_room.py`
- **should_skip_room_validation()** (5 connections) — `server/persistence/repositories/player_repository_room.py`
- **Any** (4 connections) — `server/persistence/repositories/player_repository_room.py`
- **Player** (4 connections) — `server/persistence/repositories/player_repository_room.py`
- **Validate player's current room and fix if invalid.          Args:             pl** (2 connections) — `server/persistence/repositories/player_repository.py`
- **Player room validation helpers for PlayerRepository.  Validates and fixes invali** (1 connections) — `server/persistence/repositories/player_repository_room.py`
- **Return True if room validation should be skipped (cache empty, instanced, or tut** (1 connections) — `server/persistence/repositories/player_repository_room.py`
- **Validate and fix player room, persisting the fix if needed.      Args:         r** (1 connections) — `server/persistence/repositories/player_repository_room.py`

## Relationships

- [[NPC Admin API]] (4 shared connections)
- [[Player Domain Model]] (3 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_room.py`

## Audit Trail

- EXTRACTED: 35 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
