# QuestService

> 63 nodes

## Key Concepts

- **QuestService** (76 connections) — `server/game/quest/quest_service.py`
- **Any** (22 connections)
- **QuestDefinitionSchema** (21 connections) — `server/schemas/quest/quest.py`
- **UUID** (20 connections)
- **_parse_definition()** (13 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (13 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (13 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (10 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (10 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **.turn_in_at_entity()** (6 connections) — `server/game/quest/quest_service.py`
- **_definition_completion_mode_error()** (5 connections) — `server/game/quest/quest_service.py`
- **.get_quest_log()** (5 connections) — `server/game/quest/quest_service.py`
- **.record_complete_activity()** (5 connections) — `server/game/quest/quest_service.py`
- **.record_kill()** (5 connections) — `server/game/quest/quest_service.py`
- *... and 38 more nodes in this community*

## Relationships

- [test_quest_service.py](test_quest_service.py.md) (29 shared connections)
- [quest_service.py](quest_service.py.md) (16 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [quest_rewards.py](quest_rewards.py.md) (8 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (7 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (6 shared connections)
- [test_quest_service_collect.py](test_quest_service_collect.py.md) (4 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [test_quest_start_by_trigger_then_abandon](test_quest_start_by_trigger_then_abandon.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (2 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_service.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 199 (87%)
- INFERRED: 31 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*