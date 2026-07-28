# Container Data Models

> 77 nodes · cohesion 0.05

## Key Concepts

- **container_persistence_async.py** (33 connections) — `server/persistence/container_persistence_async.py`
- **container_query_helpers_async.py** (23 connections) — `server/persistence/container_query_helpers_async.py`
- **container_repository.py** (23 connections) — `server/persistence/repositories/container_repository.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **get_container_async()** (16 connections) — `server/persistence/container_persistence_async.py`
- **_build_container_data_from_row_async()** (14 connections) — `server/persistence/container_query_helpers_async.py`
- **create_container_async()** (13 connections) — `server/persistence/container_persistence_async.py`
- **container_data.py** (12 connections) — `server/persistence/container_data.py`
- **_finalize_container_creation()** (11 connections) — `server/persistence/container_persistence_async.py`
- **Any** (11 connections)
- **update_container_async()** (11 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **get_containers_by_entity_id_async()** (10 connections) — `server/persistence/container_query_helpers_async.py`
- **get_decayed_containers_async()** (10 connections) — `server/persistence/container_query_helpers_async.py`
- **_container_data_to_dict()** (10 connections) — `server/persistence/repositories/container_repository.py`
- **_populate_container_items_async()** (9 connections) — `server/persistence/container_persistence_async.py`
- **get_containers_by_room_id_async()** (9 connections) — `server/persistence/container_query_helpers_async.py`
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **delete_container_async()** (8 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (8 connections)
- **_call_create_container_procedure()** (7 connections) — `server/persistence/container_persistence_async.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- *... and 52 more nodes in this community*

## Relationships

- [Container Persistence Queries](Container_Persistence_Queries.md) (38 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (31 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (12 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (6 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (4 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Warning Fixes Session](Warning_Fixes_Session.md) (2 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`
- `server/persistence/container_query_helpers_async.py`
- `server/persistence/repositories/container_repository.py`

## Audit Trail

- EXTRACTED: 404 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*