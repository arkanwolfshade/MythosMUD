# Communication Command Handlers

> 65 nodes · cohesion 0.06

## Key Concepts

- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **TestOpenContainer** (20 connections) — `server/tests/unit/api/test_containers.py`
- **OpenContainerRequest** (17 connections) — `server/api/container_models.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **_convert_inventory_list_to_inventory_stacks()** (11 connections) — `server/api/container_endpoints_basic.py`
- **register_basic_endpoints()** (10 connections) — `server/api/container_endpoints_basic.py`
- **ContainerCloseResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerData** (10 connections) — `server/schemas/containers/container_data.py`
- **InventoryStack** (10 connections) — `server/schemas/containers/container_data.py`
- **containers.py** (9 connections) — `server/api/containers.py`
- **container.py** (9 connections) — `server/schemas/containers/container.py`
- **register_loot_endpoints()** (8 connections) — `server/api/container_endpoints_loot.py`
- **_build_container_data_from_dict()** (7 connections) — `server/api/container_endpoints_basic.py`
- **container_data.py** (7 connections) — `server/schemas/containers/container_data.py`
- **__init__.py** (7 connections) — `server/schemas/containers/__init__.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **.test_open_container_access_denied()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_locked()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_not_found()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_rate_limit()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **Any** (5 connections)
- *... and 40 more nodes in this community*

## Relationships

- [Container API Endpoints](Container_API_Endpoints.md) (30 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (25 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (18 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (5 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (5 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (3 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 295 (85%)
- INFERRED: 53 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*