# Realtime Game State

> 10 nodes · cohesion 0.20

## Key Concepts

- **._convert_player_uuids_to_names()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **Get NPC names for multiple NPCs in a batch operation.          Args:** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get player name and add grace period indicators if applicable.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert player UUIDs to names in room_data.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert player UUIDs and NPC IDs in room_data to names.          CRITICAL: NEVER** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get a player from the persistence layer (async version).          Args:** (1 connections) — `server/realtime/integration/game_state_provider.py`

## Relationships

- [[Game State Provider]] (13 shared connections)
- [[Look Command Helpers]] (2 shared connections)
- [[NPC Occupant Verification]] (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
