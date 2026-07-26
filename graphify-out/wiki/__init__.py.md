# __init__.py

> 53 nodes · cohesion 0.05

## Key Concepts

- **__init__.py** (32 connections) — `server/persistence/__init__.py`
- **PlayerRepositoryProtocol** (21 connections) — `server/persistence/protocols.py`
- **ContainerRepository** (16 connections) — `server/persistence/repositories/container_repository.py`
- **protocols.py** (11 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **RoomRepositoryProtocol** (9 connections) — `server/persistence/protocols.py`
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **container_create_params.py** (6 connections) — `server/persistence/container_create_params.py`
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
- **.get_room_by_id()** (3 connections) — `server/persistence/protocols.py`
- **.list_rooms()** (3 connections) — `server/persistence/protocols.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/container_repository.py`
- *... and 28 more nodes in this community*

## Relationships

- [container_persistence.py](container_persistence.py.md) (13 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [container_persistence_async.py](container_persistence_async.py.md) (12 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [Room](Room.md) (3 shared connections)
- [HealthRepository](HealthRepository.md) (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_create_params.py`
- `server/persistence/protocols.py`
- `server/persistence/repositories/container_repository.py`

## Audit Trail

- EXTRACTED: 195 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*