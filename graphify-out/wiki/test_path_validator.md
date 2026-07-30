# test path validator

> 13 nodes

## Key Concepts

- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **_convert_inventory_list_to_inventory_stacks()** (11 connections) — `server/api/container_endpoints_basic.py`
- **_build_container_data_from_dict()** (7 connections) — `server/api/container_endpoints_basic.py`
- **Any** (5 connections)
- **_convert_uuid_to_string()** (4 connections) — `server/api/container_endpoints_basic.py`
- **_convert_datetime_to_iso()** (4 connections) — `server/api/container_endpoints_basic.py`
- **InventoryStack** (2 connections)
- **ContainerData** (2 connections)
- **Convert UUID-like object to string if it has __str__ method.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Convert datetime object to ISO format string.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Build ContainerData model from dictionary and converted values.** (1 connections) — `server/api/container_endpoints_basic.py`
- **Convert container dictionary from ContainerComponent.model_dump() to ContainerDa** (1 connections) — `server/api/container_endpoints_basic.py`
- **Convert list of inventory dicts to InventoryStack models.** (1 connections) — `server/api/container_endpoints_basic.py`

## Relationships

- [BaseCommand](BaseCommand.md) (10 shared connections)
- [APIRouter](APIRouter.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`

## Audit Trail

- EXTRACTED: 50 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*