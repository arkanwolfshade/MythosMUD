# test_metrics.py

> 51 nodes · cohesion 0.07

## Key Concepts

- **ItemFactory** (35 connections) — `server/game/items/item_factory.py`
- **PrototypeRegistryError** (26 connections) — `server/game/items/prototype_registry.py`
- **item_factory.py** (21 connections) — `server/game/items/item_factory.py`
- **room_item_seeder.py** (21 connections) — `server/services/room_item_seeder.py`
- **test_item_factory.py** (14 connections) — `server/tests/unit/game/test_item_factory.py`
- **ItemFactoryError** (13 connections) — `server/game/items/item_factory.py`
- **items/__init__.py** (11 connections) — `server/game/items/__init__.py`
- **ItemInstance** (9 connections) — `server/game/items/item_instance.py`
- **.create_instance()** (8 connections) — `server/game/items/item_factory.py`
- **item_instance.py** (5 connections) — `server/game/items/item_instance.py`
- **_factory_for()** (5 connections) — `server/tests/unit/game/test_item_factory.py`
- **SimpleNamespace** (5 connections)
- **test_item_instance.py** (5 connections) — `server/tests/unit/game/test_item_instance.py`
- **.build_inner_container()** (4 connections) — `server/game/items/item_factory.py`
- **._build_instance_metadata()** (4 connections) — `server/game/items/item_factory.py`
- **_item_entries()** (4 connections) — `server/services/room_item_seeder.py`
- **test_create_instance_prototype_not_found()** (4 connections) — `server/tests/unit/game/test_item_factory.py`
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
- **._resolve_stack_slot()** (3 connections) — `server/game/items/item_factory.py`
- **Any** (3 connections)
- **.to_inventory_stack()** (3 connections) — `server/game/items/item_instance.py`
- **factory()** (3 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_instance_builds_inner_container_from_prototype()** (3 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_instance_invalid_quantity()** (3 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_instance_success()** (3 connections) — `server/tests/unit/game/test_item_factory.py`
- *... and 26 more nodes in this community*

## Relationships

- [PlayerDeathService](PlayerDeathService.md) (18 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (17 shared connections)
- [npc_database.py](npc_database.py.md) (6 shared connections)
- [Room](Room.md) (4 shared connections)
- [useGameClientV2ContainerNetworkPhase.ts](useGameClientV2ContainerNetworkPhase.ts.md) (4 shared connections)
- [run_flee_effect](run_flee_effect.md) (4 shared connections)
- [description](description.md) (3 shared connections)
- [item_prototype.schema.json](item_prototype.schema.json.md) (3 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [items/catalog_dml.py](items-catalog_dml.py.md) (2 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (2 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (2 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/prototype_registry.py`
- `server/services/room_item_seeder.py`
- `server/tests/unit/game/test_item_factory.py`
- `server/tests/unit/game/test_item_instance.py`

## Audit Trail

- EXTRACTED: 139 (85%)
- INFERRED: 24 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*