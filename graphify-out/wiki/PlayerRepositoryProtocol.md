# PlayerRepositoryProtocol

> 23 nodes

## Key Concepts

- **PlayerRepositoryProtocol** (23 connections) — `server/persistence/protocols.py`
- **test_protocol_ellipsis_bodies_via_unbound_methods()** (22 connections) — `server/tests/unit/persistence/test_protocols.py`
- **Player** (11 connections)
- **.get_active_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_name()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_in_room()** (4 connections) — `server/persistence/protocols.py`
- **.save_player()** (4 connections) — `server/persistence/protocols.py`
- **.save_players()** (4 connections) — `server/persistence/protocols.py`
- **.validate_and_fix_player_room()** (4 connections) — `server/persistence/protocols.py`
- **.list_players()** (3 connections) — `server/persistence/protocols.py`
- **Protocol** (2 connections)
- **Protocol for player persistence operations. Defines the contract used by…** (1 connections) — `server/persistence/protocols.py`
- **Get the first active player for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get all players (including deleted) for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get active (non-deleted) players for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get an active player by name (case-insensitive).** (1 connections) — `server/persistence/protocols.py`
- **Save a player to the database.** (1 connections) — `server/persistence/protocols.py`
- **Save multiple players in a single transaction.** (1 connections) — `server/persistence/protocols.py`
- **Get all players in a specific room.** (1 connections) — `server/persistence/protocols.py`
- **Validate player's current room and fix if invalid.** (1 connections) — `server/persistence/protocols.py`
- **Exercise Protocol method bodies (`...`) for line coverage.** (1 connections) — `server/tests/unit/persistence/test_protocols.py`

## Relationships

- [UUID](UUID.md) (12 shared connections)
- [test_protocols.py](test_protocols.py.md) (4 shared connections)
- [Player](Player.md) (2 shared connections)
- [.get_room_by_id](get_room_by_id.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 59 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*