# QuestService

> 103 nodes

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
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **._apply_item_reward()** (8 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (7 connections) — `server/game/quest/quest_service.py`
- *... and 78 more nodes in this community*

## Relationships

- [test_quest_service.py](test_quest_service.py.md) (31 shared connections)
- [quest_commands.py](quest_commands.py.md) (13 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (11 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (9 shared connections)
- [collect_inventory.py](collect_inventory.py.md) (7 shared connections)
- [PlayerService](PlayerService.md) (6 shared connections)
- [test_quest_service_collect.py](test_quest_service_collect.py.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [.__post_init__](__post_init__.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/quest/__init__.py`
- `server/game/quest/quest_chat_notify.py`
- `server/game/quest/quest_service.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 291 (90%)
- INFERRED: 33 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*