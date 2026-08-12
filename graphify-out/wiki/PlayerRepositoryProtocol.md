# PlayerRepositoryProtocol

> 32 nodes

## Key Concepts

- **PlayerRepositoryProtocol** (21 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **UUID** (6 connections)
- **.get_players_batch()** (4 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (4 connections) — `server/persistence/protocols.py`
- **.delete_player()** (3 connections) — `server/persistence/protocols.py`
- **.get_active_players_by_user_id()** (3 connections) — `server/persistence/protocols.py`
- **.get_player_by_id()** (3 connections) — `server/persistence/protocols.py`
- **.get_player_by_name()** (3 connections) — `server/persistence/protocols.py`
- **.get_player_by_user_id()** (3 connections) — `server/persistence/protocols.py`
- **.get_players_by_user_id()** (3 connections) — `server/persistence/protocols.py`
- **.get_players_in_room()** (3 connections) — `server/persistence/protocols.py`
- **.save_player()** (3 connections) — `server/persistence/protocols.py`
- **.save_players()** (3 connections) — `server/persistence/protocols.py`
- **.soft_delete_player()** (3 connections) — `server/persistence/protocols.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/persistence/protocols.py`
- **.list_players()** (2 connections) — `server/persistence/protocols.py`
- **datetime** (2 connections)
- **Protocol** (2 connections)
- **Protocol for player persistence operations. Defines the contract used by…** (1 connections) — `server/persistence/protocols.py`
- **Get the first active player for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get all players (including deleted) for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get active (non-deleted) players for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get an active player by name (case-insensitive).** (1 connections) — `server/persistence/protocols.py`
- **Save a player to the database.** (1 connections) — `server/persistence/protocols.py`
- *... and 7 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [Player](Player.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*