# Exploration Command Models

> 30 nodes · cohesion 0.10

## Key Concepts

- **collect_inventory.py** (17 connections) — `server/game/quest/collect_inventory.py`
- **Any** (14 connections)
- **consume_prototype_from_player()** (13 connections) — `server/game/quest/collect_inventory.py`
- **count_prototype_in_stacks()** (12 connections) — `server/game/quest/collect_inventory.py`
- **collect_player_stacks()** (10 connections) — `server/game/quest/collect_inventory.py`
- **test_collect_inventory.py** (10 connections) — `server/tests/unit/game/test_collect_inventory.py`
- **_consume_from_stack_list()** (8 connections) — `server/game/quest/collect_inventory.py`
- **_stack_prototype_id()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_stack_quantity()** (5 connections) — `server/game/quest/collect_inventory.py`
- **.get_equipped_items()** (5 connections) — `server/models/player.py`
- **.set_equipped_items()** (3 connections) — `server/models/player.py`
- **.set_inventory()** (3 connections) — `server/models/player.py`
- **test_collect_player_stacks_merges_inventory_and_equipped()** (3 connections) — `server/tests/unit/game/test_collect_inventory.py`
- **test_consume_prototype_from_player_insufficient_returns_false()** (3 connections) — `server/tests/unit/game/test_collect_inventory.py`
- **test_consume_prototype_from_player_partial_stack()** (3 connections) — `server/tests/unit/game/test_collect_inventory.py`
- **test_count_prototype_in_stacks_nested_container()** (3 connections) — `server/tests/unit/game/test_collect_inventory.py`
- **test_count_prototype_in_stacks_top_level()** (3 connections) — `server/tests/unit/game/test_collect_inventory.py`
- **Inventory helpers for collect_n quest goals.  Counts and consumes items by proto** (1 connections) — `server/game/quest/collect_inventory.py`
- **Return prototype id from a stack dict.** (1 connections) — `server/game/quest/collect_inventory.py`
- **Return non-negative quantity for a stack.** (1 connections) — `server/game/quest/collect_inventory.py`
- **Return inner_container.items as dicts, or None if absent.** (1 connections) — `server/game/quest/collect_inventory.py`
- **Set player inventory from list.** (1 connections) — `server/models/player.py`
- **Return equipped items mapping.          On load, _equipped_items may be None; po** (1 connections) — `server/models/player.py`
- **Assign equipped items mapping.** (1 connections) — `server/models/player.py`
- **Unit tests for collect_n inventory helpers.** (1 connections) — `server/tests/unit/game/test_collect_inventory.py`
- *... and 5 more nodes in this community*

## Relationships

- [Quest Service Core](Quest_Service_Core.md) (5 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (1 shared connections)

## Source Files

- `server/game/quest/collect_inventory.py`
- `server/models/player.py`
- `server/tests/unit/game/test_collect_inventory.py`

## Audit Trail

- EXTRACTED: 127 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*