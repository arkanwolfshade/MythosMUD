# collect inventory game

> 61 nodes

## Key Concepts

- **quest_service.py** (32 connections) — `server/game/quest/quest_service.py`
- **collect_inventory.py** (17 connections) — `server/game/quest/collect_inventory.py`
- **Any** (14 connections)
- **consume_prototype_from_player()** (13 connections) — `server/game/quest/collect_inventory.py`
- **count_prototype_in_stacks()** (12 connections) — `server/game/quest/collect_inventory.py`
- **collect_player_stacks()** (10 connections) — `server/game/quest/collect_inventory.py`
- **test_collect_inventory.py** (10 connections) — `server/tests/unit/game/test_collect_inventory.py`
- **_consume_from_stack_list()** (8 connections) — `server/game/quest/collect_inventory.py`
- **_snapshot_holdings()** (7 connections) — `server/game/quest/collect_inventory.py`
- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **_apply_holdings()** (6 connections) — `server/game/quest/collect_inventory.py`
- **_stack_prototype_id()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_stack_quantity()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_nested_item_dicts()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_consume_from_equipped()** (5 connections) — `server/game/quest/collect_inventory.py`
- **_collect_goal_prototype_id()** (5 connections) — `server/game/quest/quest_service.py`
- **.get_equipped_items()** (5 connections) — `server/models/player.py`
- **_dict_stacks_from_callable()** (4 connections) — `server/game/quest/collect_inventory.py`
- **_dict_stacks_from_equipped()** (4 connections) — `server/game/quest/collect_inventory.py`
- **_deepcopy_dict_stacks()** (4 connections) — `server/game/quest/collect_inventory.py`
- **_deepcopy_equipped_map()** (4 connections) — `server/game/quest/collect_inventory.py`
- **_collect_goal_required_count()** (4 connections) — `server/game/quest/quest_service.py`
- **__init__.py** (3 connections) — `server/game/quest/__init__.py`
- **.set_inventory()** (3 connections) — `server/models/player.py`
- *... and 36 more nodes in this community*

## Relationships

- [quest game service](quest_game_service.md) (18 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (6 shared connections)
- [combat models rationale](combat_models_rationale.md) (3 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [message realtime messaging](message_realtime_messaging.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)
- [collect quest service](collect_quest_service.md) (1 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)

## Source Files

- `server/game/quest/__init__.py`
- `server/game/quest/collect_inventory.py`
- `server/game/quest/quest_service.py`
- `server/models/player.py`
- `server/tests/unit/game/test_collect_inventory.py`

## Audit Trail

- EXTRACTED: 238 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*