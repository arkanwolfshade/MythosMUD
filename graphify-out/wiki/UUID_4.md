# UUID

> 6 nodes

## Key Concepts

- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **_collect_goal_prototype_id()** (5 connections) — `server/game/quest/quest_service.py`
- **_collect_goal_required_count()** (4 connections) — `server/game/quest/quest_service.py`
- **Return collect_n prototype id from goal target or config.** (1 connections) — `server/game/quest/quest_service.py`
- **Return required count for a collect_n goal.** (1 connections) — `server/game/quest/quest_service.py`
- **Consume each collect_n goal from player holdings. Return error dict or None.** (1 connections) — `server/game/quest/quest_service.py`

## Relationships

- [QuestCompleted](QuestCompleted.md) (8 shared connections)
- [collect inventory](collect_inventory.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_service.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*