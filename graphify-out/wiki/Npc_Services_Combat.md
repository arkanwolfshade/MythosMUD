# Npc Services Combat

> 28 nodes

## Key Concepts

- **PrototypeRegistryError** (19 connections) — `server/game/items/prototype_registry.py`
- **item_factory.py** (14 connections) — `server/game/items/item_factory.py`
- **ItemFactory** (13 connections) — `server/game/items/item_factory.py`
- **__init__.py** (11 connections) — `server/game/items/__init__.py`
- **ItemFactoryError** (9 connections) — `server/game/items/item_factory.py`
- **.create_instance()** (7 connections) — `server/game/items/item_factory.py`
- **ItemInstance** (7 connections) — `server/game/items/item_instance.py`
- **initialize_components()** (5 connections) — `server/game/items/component_hooks.py`
- **._build_instance_metadata()** (4 connections) — `server/game/items/item_factory.py`
- **item_instance.py** (4 connections) — `server/game/items/item_instance.py`
- **._resolve_stack_slot()** (3 connections) — `server/game/items/item_factory.py`
- **Any** (3 connections)
- **.to_inventory_stack()** (3 connections) — `server/game/items/item_instance.py`
- **Item system package.  This module exposes the prototype schema and registry util** (1 connections) — `server/game/items/__init__.py`
- **Any** (1 connections)
- **Prepare component state metadata for a new item instance.      This routine curr** (1 connections) — `server/game/items/component_hooks.py`
- **Exception** (1 connections)
- **ItemInstance** (1 connections)
- **Item factory for creating item instances from prototypes.  This module provide** (1 connections) — `server/game/items/item_factory.py`
- **Raised when the factory cannot produce a valid instance.** (1 connections) — `server/game/items/item_factory.py`
- **Factory responsible for instantiating runtime item instances.** (1 connections) — `server/game/items/item_factory.py`
- **Create an item instance from a prototype.** (1 connections) — `server/game/items/item_factory.py`
- **Any** (1 connections)
- **Item instance model for runtime item representation.  This module defines the It** (1 connections) — `server/game/items/item_instance.py`
- **Runtime representation of an item created from a prototype.** (1 connections) — `server/game/items/item_instance.py`
- *... and 3 more nodes in this community*

## Relationships

- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (7 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (4 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (2 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (2 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (1 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/component_hooks.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/prototype_registry.py`

## Audit Trail

- EXTRACTED: 104 (89%)
- INFERRED: 13 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*