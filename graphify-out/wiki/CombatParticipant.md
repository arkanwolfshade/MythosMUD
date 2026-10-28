# CombatParticipant

> 106 nodes · cohesion 0.04

## Key Concepts

- **LootAllRequest** (59 connections) — `server/api/container_models.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (32 connections) — `server/api/container_endpoints_loot.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **asyncio** (14 connections)
- **apply_rate_limiting_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **asyncio** (9 connections)
- **asyncio** (7 connections)
- **.test_loot_all_items_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_container_not_found()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_locked_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **_build_loot_all_response()** (6 connections) — `server/api/container_endpoints_loot.py`
- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
- **Any** (6 connections)
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_generic_exception()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_player_not_found()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_rate_limit_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- *... and 81 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (29 shared connections)
- [test_look_player.py](test_look_player.py.md) (27 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (15 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (14 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (13 shared connections)
- [generate_arkham_grid.py](generate_arkham_grid.py.md) (8 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (8 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [AttributeError](AttributeError.md) (4 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [Room](Room.md) (3 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 320 (92%)
- INFERRED: 27 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*