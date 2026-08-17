# PlayerRepositoryProtocol

> 34 nodes

## Key Concepts

- **PlayerRepositoryProtocol** (23 connections) — `server/persistence/protocols.py`
- **test_protocol_ellipsis_bodies_via_unbound_methods()** (22 connections) — `server/tests/unit/persistence/test_protocols.py`
- **Player** (11 connections)
- **UUID** (6 connections)
- **.get_players_batch()** (5 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (5 connections) — `server/persistence/protocols.py`
- **.delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_name()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_in_room()** (4 connections) — `server/persistence/protocols.py`
- **.save_player()** (4 connections) — `server/persistence/protocols.py`
- **.save_players()** (4 connections) — `server/persistence/protocols.py`
- **.soft_delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.validate_and_fix_player_room()** (4 connections) — `server/persistence/protocols.py`
- **.list_players()** (3 connections) — `server/persistence/protocols.py`
- **datetime** (2 connections)
- **Protocol** (2 connections)
- **Protocol for player persistence operations. Defines the contract used by…** (1 connections) — `server/persistence/protocols.py`
- **Get the first active player for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get all players (including deleted) for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get active (non-deleted) players for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get an active player by name (case-insensitive).** (1 connections) — `server/persistence/protocols.py`
- *... and 9 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)
- [test_protocols.py](test_protocols.py.md) (4 shared connections)
- [.get_room_by_id](get_room_by_id.md) (2 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 71 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*