# auth endpoints rationale

> 27 nodes

## Key Concepts

- **ContainerData** (34 connections) — `server/persistence/container_data.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **container_data.py** (12 connections) — `server/persistence/container_data.py`
- **test_update_container_uuid_string_conversion()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_missing_item_instance_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_only_prototype_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_container_data_to_dict()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_container_data_to_dict_none_values()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_get_containers_by_room_id_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_entity_id_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_container_data_init()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **.__init__()** (3 connections) — `server/persistence/container_data.py`
- **.to_dict()** (2 connections) — `server/persistence/container_data.py`
- **Container data class for persistence operations.** (1 connections) — `server/persistence/container_data.py`
- **Identity and placement fields for a container row.** (1 connections) — `server/persistence/container_data.py`
- **Optional payload and timestamps for a container row.** (1 connections) — `server/persistence/container_data.py`
- **Data class for container information.** (1 connections) — `server/persistence/container_data.py`
- **Convert container data to dictionary.          Returns dictionary with model fie** (1 connections) — `server/persistence/container_data.py`
- **Test get_containers_by_room_id successfully retrieves containers.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test get_containers_by_entity_id successfully retrieves containers.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container handles UUID to string conversion.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container skips items without item_instance_id or prototype_id.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container handles items with only prototype_id (no item_instance_id)** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test ContainerData initialization.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- *... and 2 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (20 shared connections)
- [persistence container item](persistence_container_item.md) (19 shared connections)
- [follow service game](follow_service_game.md) (11 shared connections)
- [container sql injection](container_sql_injection.md) (11 shared connections)
- [persistence container extended](persistence_container_extended.md) (7 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (3 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`

## Audit Trail

- EXTRACTED: 128 (90%)
- INFERRED: 15 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*