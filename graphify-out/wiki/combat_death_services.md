# combat death services

> 6 nodes

## Key Concepts

- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._all_required_completed()** (4 connections) — `server/game/quest/quest_service.py`
- **._any_required_completed()** (4 connections) — `server/game/quest/quest_service.py`
- **Return True if the player has completed every quest in quest_ids.** (1 connections) — `server/game/quest/quest_service.py`
- **Return True if the player has completed at least one quest in quest_ids.** (1 connections) — `server/game/quest/quest_service.py`
- **Check DAG: requires_all (all must be completed) and requires_any (at least one).** (1 connections) — `server/game/quest/quest_service.py`

## Relationships

- [quest game service](quest_game_service.md) (5 shared connections)
- [quest service game](quest_service_game.md) (3 shared connections)

## Source Files

- `server/game/quest/quest_service.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*