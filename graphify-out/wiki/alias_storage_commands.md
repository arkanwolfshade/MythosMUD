# alias storage commands

> 67 nodes

## Key Concepts

- **ContainerService** (78 connections) — `server/services/container_service.py`
- **.transfer_from_container()** (18 connections) — `server/services/container_service.py`
- **UUID** (17 connections)
- **.open_container()** (15 connections) — `server/services/container_service.py`
- **Any** (13 connections)
- **.transfer_to_container()** (13 connections) — `server/services/container_service.py`
- **.lock_container()** (12 connections) — `server/services/container_service.py`
- **.unlock_container()** (12 connections) — `server/services/container_service.py`
- **.loot_all()** (11 connections) — `server/services/container_service.py`
- **._validate_container_access()** (11 connections) — `server/services/container_service.py`
- **_filter_container_data()** (10 connections) — `server/services/container_service.py`
- **.is_admin()** (10 connections) — `server/services/user_manager.py`
- **._remove_item_from_container()** (8 connections) — `server/services/container_service.py`
- **ContainerComponent** (8 connections)
- **._add_item_to_player_inventory()** (8 connections) — `server/services/container_service.py`
- **._persist_and_audit_transfer_from_container()** (8 connections) — `server/services/container_service.py`
- **_get_enum_value()** (7 connections) — `server/services/container_service.py`
- **._verify_container_open()** (7 connections) — `server/services/container_service.py`
- **._validate_proximity()** (7 connections) — `server/services/container_service.py`
- **._validate_ownership()** (7 connections) — `server/services/container_service.py`
- **._can_unlock_container()** (7 connections) — `server/services/container_service.py`
- **._validate_container_close()** (6 connections) — `server/services/container_service.py`
- **._audit_log_container_close()** (6 connections) — `server/services/container_service.py`
- **.close_container()** (6 connections) — `server/services/container_service.py`
- **InventoryStack** (6 connections)
- *... and 42 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (37 shared connections)
- [Loot Generation](Loot_Generation.md) (20 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (19 shared connections)
- [Database Config](Database_Config.md) (13 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (4 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (3 shared connections)
- [services user manager](services_user_manager.md) (3 shared connections)
- [container events rationale](container_events_rationale.md) (2 shared connections)
- [commands inventory command](commands_inventory_command.md) (1 shared connections)
- [caching lru cache](caching_lru_cache.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/user_manager.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 308 (80%)
- INFERRED: 77 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*