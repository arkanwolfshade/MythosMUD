# QuestService

> 92 nodes

## Key Concepts

- **QuestService** (79 connections) — `server/game/quest/quest_service.py`
- **quest_service.py** (32 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (13 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (13 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (13 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (11 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (8 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._turn_in_inventory_full_error()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (6 connections) — `server/game/quest/quest_service.py`
- *... and 67 more nodes in this community*

## Relationships

- [test_quest_service.py](test_quest_service.py.md) (31 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (13 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [collect_inventory.py](collect_inventory.py.md) (7 shared connections)
- [User](User.md) (6 shared connections)
- [test_quest_service_collect.py](test_quest_service_collect.py.md) (5 shared connections)
- [quest_commands.py](quest_commands.py.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [.__post_init__](__post_init__.md) (3 shared connections)
- [test_quest_start_by_trigger_then_abandon](test_quest_start_by_trigger_then_abandon.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 264 (89%)
- INFERRED: 33 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*