# Room Occupancy Class

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

- [Container Persistence Queries](Container_Persistence_Queries.md) (13 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (12 shared connections)
- [Container Data Models](Container_Data_Models.md) (12 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (8 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (4 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (4 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (3 shared connections)
- [Health Cold Resistance](Health_Cold_Resistance.md) (1 shared connections)

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