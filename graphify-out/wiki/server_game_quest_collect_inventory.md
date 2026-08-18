# server game quest collect inventory

> 59 nodes

## Key Concepts

- **quest_service.py** (32 connections) — `server/game/quest/quest_service.py`
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

- [server game quest quest service](server_game_quest_quest_service.md) (18 shared connections)
- [server container bundles chat chatbundle](server_container_bundles_chat_chatbundle.md) (6 shared connections)
- [server async persistence](server_async_persistence.md) (2 shared connections)
- [integration](integration.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (2 shared connections)
- [server api players](server_api_players.md) (1 shared connections)
- [exitstack](exitstack.md) (1 shared connections)
- [server dependencies](server_dependencies.md) (1 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (1 shared connections)

## Source Files

- `server/game/quest/__init__.py`
- `server/game/quest/collect_inventory.py`
- `server/game/quest/quest_service.py`
- `server/models/player.py`
- `server/tests/unit/game/test_collect_inventory.py`

## Audit Trail

- EXTRACTED: 137 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*