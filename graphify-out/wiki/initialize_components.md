# initialize_components

> 18 nodes

## Key Concepts

- **initialize_components()** (9 connections) — `server/game/items/component_hooks.py`
- **.create_instance()** (8 connections) — `server/game/items/item_factory.py`
- **component_hooks.py** (6 connections) — `server/game/items/component_hooks.py`
- **test_component_hooks.py** (6 connections) — `server/tests/unit/game/items/test_component_hooks.py`
- **.build_inner_container()** (4 connections) — `server/game/items/item_factory.py`
- **._build_instance_metadata()** (4 connections) — `server/game/items/item_factory.py`
- **._resolve_stack_slot()** (3 connections) — `server/game/items/item_factory.py`
- **Any** (3 connections)
- **test_initialize_components_empty_prototype()** (2 connections) — `server/tests/unit/game/items/test_component_hooks.py`
- **test_initialize_components_merges_overrides()** (2 connections) — `server/tests/unit/game/items/test_component_hooks.py`
- **test_initialize_components_records_prototype_components()** (2 connections) — `server/tests/unit/game/items/test_component_hooks.py`
- **ItemInstance** (1 connections)
- **Any** (1 connections)
- **Component hook coordination for freshly minted item instances.** (1 connections) — `server/game/items/component_hooks.py`
- **Prepare component state metadata for a new item instance. This routine…** (1 connections) — `server/game/items/component_hooks.py`
- **Empty nested container defined by a prototype's ``metadata.container``, or None.** (1 connections) — `server/game/items/item_factory.py`
- **Create an item instance from a prototype.** (1 connections) — `server/game/items/item_factory.py`
- **Unit tests for item component hooks.** (1 connections) — `server/tests/unit/game/items/test_component_hooks.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [ItemFactory](ItemFactory.md) (4 shared connections)
- [Room](Room.md) (1 shared connections)
- [test_item_factory.py](test_item_factory.py.md) (1 shared connections)

## Source Files

- `server/game/items/component_hooks.py`
- `server/game/items/item_factory.py`
- `server/tests/unit/game/items/test_component_hooks.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*