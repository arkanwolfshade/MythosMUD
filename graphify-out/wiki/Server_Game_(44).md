# Server Game (44)

> 12 nodes

## Key Concepts

- **quest_service.py** (24 connections) — `server/game/quest/quest_service.py`
- **_call_add_item_to_inventory()** (5 connections) — `server/game/quest/quest_service.py`
- **_definition_completion_mode_error()** (5 connections) — `server/game/quest/quest_service.py`
- **_goal_activity_target()** (4 connections) — `server/game/quest/quest_service.py`
- **_collect_goal_required_count()** (4 connections) — `server/game/quest/quest_service.py`
- **__init__.py** (3 connections) — `server/game/quest/__init__.py`
- **Quest subsystem: service, goal progression, rewards.** (1 connections) — `server/game/quest/__init__.py`
- **Quest service: start, progress, complete, turn-in, abandon, and quest log.  Reso** (1 connections) — `server/game/quest/quest_service.py`
- **Call inventory add_item_to_inventory (fn from getattr). Isolates Any call for ty** (1 connections) — `server/game/quest/quest_service.py`
- **Return error message if auto_complete and turn_in_entities are mutually invalid.** (1 connections) — `server/game/quest/quest_service.py`
- **Resolve the activity/npc target string for a progress goal.** (1 connections) — `server/game/quest/quest_service.py`
- **Return required count for a collect_n goal.** (1 connections) — `server/game/quest/quest_service.py`

## Relationships

- [Server Quest](Server_Quest.md) (19 shared connections)
- [Server Game (23)](Server_Game_%2823%29.md) (4 shared connections)
- [Server Game (27)](Server_Game_%2827%29.md) (1 shared connections)
- [Server Persistence](Server_Persistence.md) (1 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server Game (15)](Server_Game_%2815%29.md) (1 shared connections)
- [Server Events](Server_Events.md) (1 shared connections)
- [Server Game (28)](Server_Game_%2828%29.md) (1 shared connections)

## Source Files

- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*