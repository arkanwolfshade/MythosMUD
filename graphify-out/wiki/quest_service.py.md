# quest_service.py

> 14 nodes

## Key Concepts

- **quest_service.py** (26 connections) — `server/game/quest/quest_service.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **_collect_goal_prototype_id()** (5 connections) — `server/game/quest/quest_service.py`
- **_collect_goal_required_count()** (4 connections) — `server/game/quest/quest_service.py`
- **_goal_activity_target()** (4 connections) — `server/game/quest/quest_service.py`
- **game/quest/__init__.py** (3 connections) — `server/game/quest/__init__.py`
- **Quest subsystem: service, goal progression, rewards.** (1 connections) — `server/game/quest/__init__.py`
- **Quest service: start, progress, complete, turn-in, abandon, and quest log.…** (1 connections) — `server/game/quest/quest_service.py`
- **Recompute collect_n goal counters from holdings into a progress dict.** (1 connections) — `server/game/quest/quest_service.py`
- **Resolve the activity/npc target string for a progress goal.** (1 connections) — `server/game/quest/quest_service.py`
- **Return collect_n prototype id from goal target or config.** (1 connections) — `server/game/quest/quest_service.py`
- **Return required count for a collect_n goal.** (1 connections) — `server/game/quest/quest_service.py`
- **Consume each collect_n goal from player holdings. Return error dict or None.** (1 connections) — `server/game/quest/quest_service.py`

## Relationships

- [QuestService](QuestService.md) (18 shared connections)
- [collect_inventory.py](collect_inventory.py.md) (6 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (1 shared connections)
- [test_quest_service_collect.py](test_quest_service_collect.py.md) (1 shared connections)

## Source Files

- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*