# schedule service services

> 35 nodes

## Key Concepts

- **ItemFactory** (17 connections) — `server/game/items/item_factory.py`
- **item_factory.py** (16 connections) — `server/game/items/item_factory.py`
- **ItemFactoryError** (15 connections) — `server/game/items/item_factory.py`
- **__init__.py** (11 connections) — `server/game/items/__init__.py`
- **test_item_factory.py** (11 connections) — `server/tests/unit/game/test_item_factory.py`
- **ItemInstance** (10 connections) — `server/game/items/item_instance.py`
- **.create_instance()** (6 connections) — `server/game/items/item_factory.py`
- **item_instance.py** (5 connections) — `server/game/items/item_instance.py`
- **test_item_instance.py** (5 connections) — `server/tests/unit/game/test_item_instance.py`
- **test_create_instance_prototype_not_found()** (4 connections) — `server/tests/unit/game/test_item_factory.py`
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
- **.to_inventory_stack()** (3 connections) — `server/game/items/item_instance.py`
- **test_create_instance_invalid_quantity()** (3 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_summon_item_instance_factory_error()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_factory_error()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **factory()** (2 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_instance_success()** (2 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_instance_with_overrides()** (2 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_item_instance_to_inventory_stack_minimal()** (2 connections) — `server/tests/unit/game/test_item_instance.py`
- **test_item_instance_to_inventory_stack_includes_optional_fields()** (2 connections) — `server/tests/unit/game/test_item_instance.py`
- **Item system package.  This module exposes the prototype schema and registry util** (1 connections) — `server/game/items/__init__.py`
- **Exception** (1 connections)
- **Any** (1 connections)
- **ItemInstance** (1 connections)
- **Item factory for creating item instances from prototypes.  This module provides** (1 connections) — `server/game/items/item_factory.py`
- *... and 10 more nodes in this community*

## Relationships

- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (15 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (4 shared connections)
- [game chat moderation](game_chat_moderation.md) (3 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [conftest eslint config](conftest_eslint_config.md) (1 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/tests/unit/commands/test_admin_summon_command.py`
- `server/tests/unit/game/test_item_factory.py`
- `server/tests/unit/game/test_item_instance.py`

## Audit Trail

- EXTRACTED: 125 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*