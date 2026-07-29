# QuestCompleted

> 84 nodes

## Key Concepts

- **QuestService** (53 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (13 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (12 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (12 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (11 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **QuestCompleted** (9 connections) — `server/events/event_types.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (7 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (6 connections) — `server/game/quest/quest_service.py`
- *... and 59 more nodes in this community*

## Relationships

- [collect inventory](collect_inventory.md) (20 shared connections)
- [main()](main%28%29.md) (7 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [Connection Manager](Connection_Manager.md) (5 shared connections)
- [notify quest abandoned()](notify_quest_abandoned%28%29.md) (5 shared connections)
- [Any](Any.md) (4 shared connections)
- [test quest service collect](test_quest_service_collect.md) (4 shared connections)
- [Base](Base.md) (4 shared connections)
- [ExitStack](ExitStack.md) (3 shared connections)
- [test quest service](test_quest_service.md) (3 shared connections)
- [test quest instance repository](test_quest_instance_repository.md) (2 shared connections)
- [lifespan](lifespan.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/quest/quest_service.py`
- `server/models/quest.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 431 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*