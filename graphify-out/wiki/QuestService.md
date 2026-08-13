# QuestService

> 79 nodes

## Key Concepts

- **QuestService** (53 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestInstance** (20 connections) — `server/models/quest.py`
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (12 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (11 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (11 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (9 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **QuestCompleted** (8 connections) — `server/events/event_types.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **.turn_in_at_entity()** (6 connections) — `server/game/quest/quest_service.py`
- **._turn_in_inventory_full_error()** (6 connections) — `server/game/quest/quest_service.py`
- *... and 54 more nodes in this community*

## Relationships

- [quest_service.py](quest_service.py.md) (20 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (9 shared connections)
- [test_quest_service_collect.py](test_quest_service_collect.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [quest_commands.py](quest_commands.py.md) (3 shared connections)
- [schemas/quest/__init__.py](schemas-quest-__init__.py.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/quest/quest_service.py`
- `server/models/quest.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 233 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*