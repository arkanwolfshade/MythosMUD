# UUID

> 11 nodes

## Key Concepts

- **UUID** (6 connections)
- **.get_players_batch()** (5 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (5 connections) — `server/persistence/protocols.py`
- **.delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.soft_delete_player()** (4 connections) — `server/persistence/protocols.py`
- **datetime** (2 connections)
- **Get multiple players by IDs in a single query.** (1 connections) — `server/persistence/protocols.py`
- **Soft delete a player (sets is_deleted=True).** (1 connections) — `server/persistence/protocols.py`
- **Delete a player from the database.** (1 connections) — `server/persistence/protocols.py`
- **Update the last_active timestamp for a player.** (1 connections) — `server/persistence/protocols.py`

## Relationships

- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (12 shared connections)
- [Player](Player.md) (2 shared connections)

## Source Files

- `server/persistence/protocols.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*