# Typography Layout Spec

> 27 nodes

## Key Concepts

- **item_factory.py** (14 connections) — `server/game/items/item_factory.py`
- **ItemFactory** (13 connections) — `server/game/items/item_factory.py`
- **__init__.py** (11 connections) — `server/game/items/__init__.py`
- **ItemFactoryError** (9 connections) — `server/game/items/item_factory.py`
- **.create_instance()** (7 connections) — `server/game/items/item_factory.py`
- **ItemInstance** (7 connections) — `server/game/items/item_instance.py`
- **initialize_components()** (5 connections) — `server/game/items/component_hooks.py`
- **._build_instance_metadata()** (4 connections) — `server/game/items/item_factory.py`
- **item_instance.py** (4 connections) — `server/game/items/item_instance.py`
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
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
- **Initialize the item factory with a prototype registry.          Args:** (1 connections) — `server/game/items/item_factory.py`
- **Create an item instance from a prototype.** (1 connections) — `server/game/items/item_factory.py`
- **Any** (1 connections)
- **Item instance model for runtime item representation.  This module defines the It** (1 connections) — `server/game/items/item_instance.py`
- *... and 2 more nodes in this community*

## Relationships

- [Quest Instance Repository](Quest_Instance_Repository.md) (7 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (5 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (1 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (1 shared connections)
- [Realtime Visual Indicator](Realtime_Visual_Indicator.md) (1 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/component_hooks.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`

## Audit Trail

- EXTRACTED: 91 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*