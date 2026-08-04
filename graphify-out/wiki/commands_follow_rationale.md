# commands follow rationale

> 38 nodes

## Key Concepts

- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **_convert_inventory_list_to_inventory_stacks()** (11 connections) — `server/api/container_endpoints_basic.py`
- **register_basic_endpoints()** (10 connections) — `server/api/container_endpoints_basic.py`
- **ContainerOpenResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerCloseResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **InventoryStack** (10 connections) — `server/schemas/containers/container_data.py`
- **ContainerData** (10 connections) — `server/schemas/containers/container_data.py`
- **container.py** (9 connections) — `server/schemas/containers/container.py`
- **_build_container_data_from_dict()** (7 connections) — `server/api/container_endpoints_basic.py`
- **__init__.py** (7 connections) — `server/schemas/containers/__init__.py`
- **container_data.py** (7 connections) — `server/schemas/containers/container_data.py`
- **Any** (5 connections)
- **_convert_uuid_to_string()** (4 connections) — `server/api/container_endpoints_basic.py`
- **_convert_datetime_to_iso()** (4 connections) — `server/api/container_endpoints_basic.py`
- **BaseModel** (4 connections)
- **BaseModel** (3 connections)
- **InnerContainer** (3 connections) — `server/schemas/containers/container_data.py`
- **InventoryStack** (2 connections)
- **ContainerData** (2 connections)
- **APIRouter** (1 connections)
- **Convert UUID-like object to string if it has __str__ method.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Convert datetime object to ISO format string.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Build ContainerData model from dictionary and converted values.** (1 connections) — `server/api/container_endpoints_basic.py`
- *... and 13 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (21 shared connections)
- [task registry app](task_registry_app.md) (8 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (5 shared connections)
- [command factories communication](command_factories_communication.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`

## Audit Trail

- EXTRACTED: 139 (83%)
- INFERRED: 28 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*