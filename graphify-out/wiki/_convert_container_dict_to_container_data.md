# _convert_container_dict_to_container_data

> 31 nodes

## Key Concepts

- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **ContainerData** (10 connections) — `server/schemas/containers/container_data.py`
- **InventoryStack** (10 connections) — `server/schemas/containers/container_data.py`
- **_convert_inventory_list_to_inventory_stacks()** (10 connections) — `server/api/container_endpoints_basic.py`
- **ContainerOpenResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (9 connections) — `server/schemas/containers/container.py`
- **containers/container.py** (9 connections) — `server/schemas/containers/container.py`
- **_build_container_data_from_dict()** (7 connections) — `server/api/container_endpoints_basic.py`
- **containers/container_data.py** (7 connections) — `server/schemas/containers/container_data.py`
- **containers/__init__.py** (7 connections) — `server/schemas/containers/__init__.py`
- **Any** (5 connections)
- **_convert_datetime_to_iso()** (4 connections) — `server/api/container_endpoints_basic.py`
- **_convert_uuid_to_string()** (4 connections) — `server/api/container_endpoints_basic.py`
- **BaseModel** (4 connections)
- **InnerContainer** (3 connections) — `server/schemas/containers/container_data.py`
- **BaseModel** (3 connections)
- **ContainerData** (2 connections)
- **InventoryStack** (2 connections)
- **Convert list of inventory dicts to InventoryStack models.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Convert UUID-like object to string if it has __str__ method.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Convert datetime object to ISO format string.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Build ContainerData model from dictionary and converted values.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Convert container dictionary from ContainerComponent.model_dump() to…** (1 connections) — `server/api/container_endpoints_basic.py`
- **Container data schema for MythosMUD. This module defines Pydantic models for…** (1 connections) — `server/schemas/containers/container_data.py`
- **Inventory stack model for items in containers and player inventories. This…** (1 connections) — `server/schemas/containers/container_data.py`
- *... and 6 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (20 shared connections)
- [ContainerComponent](ContainerComponent.md) (9 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`

## Audit Trail

- EXTRACTED: 73 (89%)
- INFERRED: 9 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*