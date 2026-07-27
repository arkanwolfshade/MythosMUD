# Quest Service Core

> 60 nodes · cohesion 0.08

## Key Concepts

- **QuestService** (38 connections) — `server/game/quest/quest_service.py`
- **UUID** (22 connections) — `server/game/quest/quest_service.py`
- **Any** (18 connections) — `server/game/quest/quest_service.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **quest_service.py** (11 connections) — `server/game/quest/quest_service.py`
- **_parse_definition()** (10 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (10 connections) — `server/game/quest/quest_service.py`
- **QuestDefinitionSchema** (10 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (8 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (8 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (8 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (7 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (6 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **QuestInstance** (6 connections) — `server/game/quest/quest_service.py`
- **_call_add_item_to_inventory()** (5 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (5 connections) — `server/game/quest/quest_service.py`
- **._apply_spell_reward()** (5 connections) — `server/game/quest/quest_service.py`
- **._apply_xp_reward()** (5 connections) — `server/game/quest/quest_service.py`
- **.get_quest_log()** (5 connections) — `server/game/quest/quest_service.py`
- **.record_complete_activity()** (5 connections) — `server/game/quest/quest_service.py`
- *... and 35 more nodes in this community*

## Relationships

- [[Quest Instance Repository]] (6 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Game Quest Service]] (3 shared connections)
- [[Quest Flow Integration]] (3 shared connections)
- [[Distributed Event Bus]] (2 shared connections)
- [[Game Service Bundle]] (2 shared connections)
- [[Lifespan Startup Hooks]] (1 shared connections)
- [[NPC Combat Events]] (1 shared connections)
- [[Quest Schemas]] (1 shared connections)
- [[Players API Endpoints]] (1 shared connections)
- [[Quest Journal Commands]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`

## Audit Trail

- EXTRACTED: 280 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
