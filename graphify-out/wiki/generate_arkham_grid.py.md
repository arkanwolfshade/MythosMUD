# generate_arkham_grid.py

> 71 nodes · cohesion 0.05

## Key Concepts

- **container_endpoints_basic.py** (64 connections) — `server/api/container_endpoints_basic.py`
- **test_container_endpoints_basic_weapon.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_basic_weapon.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **_build_container_data_from_dict()** (10 connections) — `server/api/container_endpoints_basic.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **_convert_inventory_list_to_inventory_stacks()** (9 connections) — `server/api/container_endpoints_basic.py`
- **containers/container.py** (9 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerData** (9 connections) — `server/schemas/containers/container_data.py`
- **containers/__init__.py** (9 connections) — `server/schemas/containers/__init__.py`
- **weapon.py** (9 connections) — `server/schemas/game/weapon.py`
- **weapon_stats_from_metadata()** (9 connections) — `server/schemas/game/weapon.py`
- **_build_transfer_response()** (8 connections) — `server/api/container_endpoints_basic.py`
- **_coerce_weapon_on_item()** (8 connections) — `server/api/container_endpoints_basic.py`
- **containers/container_data.py** (8 connections) — `server/schemas/containers/container_data.py`
- **InventoryStack** (8 connections) — `server/schemas/containers/container_data.py`
- **ContainerCloseResponse** (7 connections) — `server/schemas/containers/container.py`
- **_build_open_container_response()** (6 connections) — `server/api/container_endpoints_basic.py`
- **_as_inventory_dicts()** (4 connections) — `server/api/container_endpoints_basic.py`
- **_as_str_object_mapping()** (4 connections) — `server/api/container_endpoints_basic.py`
- **BaseModel** (4 connections)
- **_apply_inventory_stack_defaults()** (3 connections) — `server/api/container_endpoints_basic.py`
- **_as_str_list()** (3 connections) — `server/api/container_endpoints_basic.py`
- **_as_str_object_dict()** (3 connections) — `server/api/container_endpoints_basic.py`
- *... and 46 more nodes in this community*

## Relationships

- [test_look_player.py](test_look_player.py.md) (23 shared connections)
- [CombatParticipant](CombatParticipant.md) (8 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (5 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [Room](Room.md) (3 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (3 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/api/test_container_endpoints_basic_weapon.py`

## Audit Trail

- EXTRACTED: 188 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*