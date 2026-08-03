# websocket helpers realtime

> 41 nodes

## Key Concepts

- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **OpenContainerRequest** (17 connections) — `server/api/container_models.py`
- **register_basic_endpoints()** (10 connections) — `server/api/container_endpoints_basic.py`
- **ContainerOpenResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerCloseResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **InventoryStack** (10 connections) — `server/schemas/containers/container_data.py`
- **ContainerData** (10 connections) — `server/schemas/containers/container_data.py`
- **container.py** (9 connections) — `server/schemas/containers/container.py`
- **__init__.py** (7 connections) — `server/schemas/containers/__init__.py`
- **container_data.py** (7 connections) — `server/schemas/containers/container_data.py`
- **.test_open_container_rate_limit()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_not_found()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_locked()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_access_denied()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_not_authenticated()** (5 connections) — `server/tests/unit/api/test_containers.py`
- **BaseModel** (4 connections)
- **.test_open_container_success()** (4 connections) — `server/tests/unit/api/test_containers.py`
- **BaseModel** (3 connections)
- **InnerContainer** (3 connections) — `server/schemas/containers/container_data.py`
- **APIRouter** (1 connections)
- **Open a container for interaction.      Initiates interaction with a container in** (1 connections) — `server/api/container_endpoints_basic.py`
- **Register basic container operation endpoints (open, transfer, close) to the rout** (1 connections) — `server/api/container_endpoints_basic.py`
- **Request model for opening a container.** (1 connections) — `server/api/container_models.py`
- *... and 16 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (23 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (20 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [admin auth service](admin_auth_service.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [container events rationale](container_events_rationale.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_models.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 159 (81%)
- INFERRED: 37 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*