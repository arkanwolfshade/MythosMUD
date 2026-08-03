# persistence protocols rationale

> 35 nodes

## Key Concepts

- **PlayerRepositoryProtocol** (25 connections) — `server/persistence/protocols.py`
- **test_protocol_ellipsis_bodies_via_unbound_methods()** (18 connections) — `server/tests/unit/persistence/test_protocols.py`
- **protocols.py** (12 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **UUID** (6 connections)
- **.get_players_batch()** (5 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (5 connections) — `server/persistence/protocols.py`
- **.get_player_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_name()** (4 connections) — `server/persistence/protocols.py`
- **.save_player()** (4 connections) — `server/persistence/protocols.py`
- **.save_players()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_in_room()** (4 connections) — `server/persistence/protocols.py`
- **.soft_delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.validate_and_fix_player_room()** (4 connections) — `server/persistence/protocols.py`
- **.list_players()** (3 connections) — `server/persistence/protocols.py`
- **datetime** (2 connections)
- **Repository protocols for MythosMUD persistence layer.  Explicit typing.Protocol** (1 connections) — `server/persistence/protocols.py`
- **Protocol for player persistence operations.      Defines the contract used by As** (1 connections) — `server/persistence/protocols.py`
- **Get the first active player for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get all players (including deleted) for a user ID.** (1 connections) — `server/persistence/protocols.py`
- **Get active (non-deleted) players for a user ID.** (1 connections) — `server/persistence/protocols.py`
- *... and 10 more nodes in this community*

## Relationships

- [config models game](config_models_game.md) (10 shared connections)
- [world models rationale](world_models_rationale.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [persistence container item](persistence_container_item.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 141 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*