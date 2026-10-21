# ExplorationCommandFactory

> 61 nodes · cohesion 0.05

## Key Concepts

- **InventoryStack** (38 connections) — `server/services/inventory_service.py`
- **InventoryService** (37 connections) — `server/services/inventory_service.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **InventorySplitError** (11 connections) — `server/services/inventory_service.py`
- **InventoryValidationError** (10 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (6 connections) — `server/services/inventory_service.py`
- **.begin_mutation()** (5 connections) — `server/services/inventory_service.py`
- **._can_merge()** (4 connections) — `server/services/inventory_service.py`
- **._extract_required_fields()** (4 connections) — `server/services/inventory_service.py`
- **._normalize_metadata()** (4 connections) — `server/services/inventory_service.py`
- **InventoryStackRequired** (4 connections) — `server/services/inventory_service.py`
- **inventory_service()** (4 connections) — `server/tests/unit/services/test_inventory_service.py`
- **InnerContainer** (3 connections) — `server/services/inventory_service.py`
- **test_add_stack_capacity_error()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_validation_error_invalid_quantity()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_validation_error_missing_field()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_capacity_error()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_index()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_quantity_negative()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_quantity_zero()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- *... and 36 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (26 shared connections)
- [TargetMatch](TargetMatch.md) (16 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (10 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (6 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (3 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (3 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Call_of_Cthulhu_Starter_Set__2026-08-12.md) (2 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [test_metadata.py](test_metadata.py.md) (1 shared connections)
- [test_look_player.py](test_look_player.py.md) (1 shared connections)
- [_parse_npc_stats_dict](_parse_npc_stats_dict.md) (1 shared connections)
- [test_command_alias.py](test_command_alias.py.md) (1 shared connections)

## Source Files

- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 131 (80%)
- INFERRED: 32 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*