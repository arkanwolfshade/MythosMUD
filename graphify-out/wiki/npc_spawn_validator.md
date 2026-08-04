# npc spawn validator

> 32 nodes

## Key Concepts

- **PrototypeRegistryError** (26 connections) — `server/game/items/prototype_registry.py`
- **prototype_registry.py** (22 connections) — `server/game/items/prototype_registry.py`
- **ItemFactory** (17 connections) — `server/game/items/item_factory.py`
- **item_factory.py** (16 connections) — `server/game/items/item_factory.py`
- **ItemFactoryError** (15 connections) — `server/game/items/item_factory.py`
- **__init__.py** (11 connections) — `server/game/items/__init__.py`
- **test_item_factory.py** (11 connections) — `server/tests/unit/game/test_item_factory.py`
- **ItemInstance** (10 connections) — `server/game/items/item_instance.py`
- **item_instance.py** (5 connections) — `server/game/items/item_instance.py`
- **test_item_instance.py** (5 connections) — `server/tests/unit/game/test_item_instance.py`
- **test_create_instance_prototype_not_found()** (4 connections) — `server/tests/unit/game/test_item_factory.py`
- **.to_inventory_stack()** (3 connections) — `server/game/items/item_instance.py`
- **test_create_instance_invalid_quantity()** (3 connections) — `server/tests/unit/game/test_item_factory.py`
- **factory()** (2 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_instance_success()** (2 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_instance_with_overrides()** (2 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_item_instance_to_inventory_stack_minimal()** (2 connections) — `server/tests/unit/game/test_item_instance.py`
- **test_item_instance_to_inventory_stack_includes_optional_fields()** (2 connections) — `server/tests/unit/game/test_item_instance.py`
- **Item system package.  This module exposes the prototype schema and registry util** (1 connections) — `server/game/items/__init__.py`
- **Exception** (1 connections)
- **Item factory for creating item instances from prototypes.  This module provides** (1 connections) — `server/game/items/item_factory.py`
- **Raised when the factory cannot produce a valid instance.** (1 connections) — `server/game/items/item_factory.py`
- **Factory responsible for instantiating runtime item instances.** (1 connections) — `server/game/items/item_factory.py`
- **Any** (1 connections)
- **Item instance model for runtime item representation.  This module defines the It** (1 connections) — `server/game/items/item_instance.py`
- *... and 7 more nodes in this community*

## Relationships

- [combat npc mixin](combat_npc_mixin.md) (14 shared connections)
- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (7 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [stats game generator](stats_game_generator.md) (5 shared connections)
- [command factories communication](command_factories_communication.md) (5 shared connections)
- [schedule service services](schedule_service_services.md) (4 shared connections)
- [game chat moderation](game_chat_moderation.md) (3 shared connections)
- [commands inventory put](commands_inventory_put.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [command commands validation](command_commands_validation.md) (1 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/prototype_registry.py`
- `server/tests/unit/game/test_item_factory.py`
- `server/tests/unit/game/test_item_instance.py`

## Audit Trail

- EXTRACTED: 153 (89%)
- INFERRED: 19 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*