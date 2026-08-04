# game chat moderation

> 14 nodes

## Key Concepts

- **initialize_components()** (9 connections) — `server/game/items/component_hooks.py`
- **component_hooks.py** (6 connections) — `server/game/items/component_hooks.py`
- **.create_instance()** (6 connections) — `server/game/items/item_factory.py`
- **test_component_hooks.py** (6 connections) — `server/tests/unit/game/items/test_component_hooks.py`
- **test_initialize_components_empty_prototype()** (2 connections) — `server/tests/unit/game/items/test_component_hooks.py`
- **test_initialize_components_records_prototype_components()** (2 connections) — `server/tests/unit/game/items/test_component_hooks.py`
- **test_initialize_components_merges_overrides()** (2 connections) — `server/tests/unit/game/items/test_component_hooks.py`
- **Any** (1 connections)
- **Component hook coordination for freshly minted item instances.** (1 connections) — `server/game/items/component_hooks.py`
- **Prepare component state metadata for a new item instance.      This routine curr** (1 connections) — `server/game/items/component_hooks.py`
- **Any** (1 connections)
- **ItemInstance** (1 connections)
- **Create an item instance from a prototype.          Args:             prototype_i** (1 connections) — `server/game/items/item_factory.py`
- **Unit tests for item component hooks.** (1 connections) — `server/tests/unit/game/items/test_component_hooks.py`

## Relationships

- [npc spawn validator](npc_spawn_validator.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)

## Source Files

- `server/game/items/component_hooks.py`
- `server/game/items/item_factory.py`
- `server/tests/unit/game/items/test_component_hooks.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*