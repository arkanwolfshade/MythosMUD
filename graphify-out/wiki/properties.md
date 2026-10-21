# properties

> 59 nodes · cohesion 0.06

## Key Concepts

- **quest_service.py** (33 connections) — `server/game/quest/quest_service.py`
- **collect_inventory.py** (17 connections) — `server/game/quest/collect_inventory.py`
- **Any** (14 connections)
- **consume_prototype_from_player()** (13 connections) — `server/game/quest/collect_inventory.py`
- **count_prototype_in_stacks()** (12 connections) — `server/game/quest/collect_inventory.py`
- **test_collect_inventory.py** (10 connections) — `server/tests/unit/game/test_collect_inventory.py`
- **collect_player_stacks()** (9 connections) — `server/game/quest/collect_inventory.py`
- **_consume_from_stack_list()** (8 connections) — `server/game/quest/collect_inventory.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **_apply_holdings()** (6 connections) — `server/game/quest/collect_inventory.py`
- **_snapshot_holdings()** (6 connections) — `server/game/quest/collect_inventory.py`
- **game/quest/__init__.py** (6 connections) — `server/game/quest/__init__.py`
- **_consume_from_equipped()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_nested_item_dicts()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_stack_prototype_id()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_stack_quantity()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_collect_goal_prototype_id()** (5 connections) — `server/game/quest/quest_service.py`
- **_deepcopy_dict_stacks()** (4 connections) — `server/game/quest/collect_inventory.py`
- **_deepcopy_equipped_map()** (4 connections) — `server/game/quest/collect_inventory.py`
- **_dict_stacks_from_callable()** (4 connections) — `server/game/quest/collect_inventory.py`
- **_dict_stacks_from_equipped()** (4 connections) — `server/game/quest/collect_inventory.py`
- **_collect_goal_required_count()** (4 connections) — `server/game/quest/quest_service.py`
- **.set_equipped_items()** (3 connections) — `server/models/player.py`
- **.set_inventory()** (3 connections) — `server/models/player.py`
- *... and 34 more nodes in this community*

## Relationships

- [item_catalog_repository.py](item_catalog_repository.py.md) (17 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (6 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [endpoints.py](endpoints.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [SpellLearningService](SpellLearningService.md) (1 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (1 shared connections)
- [test_time_bundle.py](test_time_bundle.py.md) (1 shared connections)

## Source Files

- `server/game/quest/__init__.py`
- `server/game/quest/collect_inventory.py`
- `server/game/quest/quest_service.py`
- `server/models/player.py`
- `server/tests/unit/game/test_collect_inventory.py`

## Audit Trail

- EXTRACTED: 138 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*