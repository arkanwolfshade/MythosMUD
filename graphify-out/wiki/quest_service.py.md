# quest_service.py

> 38 nodes

## Key Concepts

- **quest_service.py** (32 connections) — `server/game/quest/quest_service.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **game/quest/__init__.py** (6 connections) — `server/game/quest/__init__.py`
- **_goal_is_met()** (5 connections) — `server/game/quest/quest_chat_notify.py`
- **_collect_goal_prototype_id()** (5 connections) — `server/game/quest/quest_service.py`
- **UUID** (5 connections)
- **_progress_has_any_value()** (4 connections) — `server/game/quest/quest_chat_notify.py`
- **_collect_goal_required_count()** (4 connections) — `server/game/quest/quest_service.py`
- **Any** (4 connections)
- **_as_int()** (3 connections) — `server/game/quest/quest_chat_notify.py`
- **test_should_notify_quest_progress_milestones()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Schedule personal system chat from sync or async callers.** (1 connections) — `server/game/chat_npc_system.py`
- **Quest subsystem: service, goal progression, rewards.** (1 connections) — `server/game/quest/__init__.py`
- **Quest lifecycle and NPC quest-line chat helpers (issue #146 MVP). # group:…** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest becomes active.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat for milestone progress (first tick or goal newly met).** (1 connections) — `server/game/quest/quest_chat_notify.py`
- *... and 13 more nodes in this community*

## Relationships

- [QuestService](QuestService.md) (25 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (14 shared connections)
- [quest_commands.py](quest_commands.py.md) (7 shared connections)
- [collect_inventory.py](collect_inventory.py.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [talk_command.py](talk_command.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (1 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (1 shared connections)
- [test_quest_service_collect.py](test_quest_service_collect.py.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/__init__.py`
- `server/game/quest/quest_chat_notify.py`
- `server/game/quest/quest_service.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 123 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*