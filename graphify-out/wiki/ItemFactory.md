# ItemFactory

> 22 nodes

## Key Concepts

- **ItemFactory** (13 connections) — `server/game/items/item_factory.py`
- **items/__init__.py** (11 connections) — `server/game/items/__init__.py`
- **ItemFactoryError** (9 connections) — `server/game/items/item_factory.py`
- **ItemInstance** (7 connections) — `server/game/items/item_instance.py`
- **.create_instance()** (7 connections) — `server/game/items/item_factory.py`
- **._build_instance_metadata()** (4 connections) — `server/game/items/item_factory.py`
- **item_instance.py** (4 connections) — `server/game/items/item_instance.py`
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
- **._resolve_stack_slot()** (3 connections) — `server/game/items/item_factory.py`
- **.to_inventory_stack()** (3 connections) — `server/game/items/item_instance.py`
- **Any** (3 connections)
- **ItemInstance** (1 connections)
- **Exception** (1 connections)
- **Any** (1 connections)
- **Item system package. This module exposes the prototype schema and registry…** (1 connections) — `server/game/items/__init__.py`
- **Raised when the factory cannot produce a valid instance.** (1 connections) — `server/game/items/item_factory.py`
- **Factory responsible for instantiating runtime item instances.** (1 connections) — `server/game/items/item_factory.py`
- **Initialize the item factory with a prototype registry. Args: registry: The…** (1 connections) — `server/game/items/item_factory.py`
- **Create an item instance from a prototype.** (1 connections) — `server/game/items/item_factory.py`
- **Item instance model for runtime item representation. This module defines the…** (1 connections) — `server/game/items/item_instance.py`
- **Runtime representation of an item created from a prototype.** (1 connections) — `server/game/items/item_instance.py`
- **Convert the instance into an inventory stack payload understood by legacy…** (1 connections) — `server/game/items/item_instance.py`

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (3 shared connections)
- [prototype_registry.py](prototype_registry.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (1 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`

## Audit Trail

- EXTRACTED: 42 (86%)
- INFERRED: 7 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*