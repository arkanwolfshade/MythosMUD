# health realtime monitoring

> 6 nodes

## Key Concepts

- **__init__.py** (3 connections) — `server/game/quest/__init__.py`
- **.set_spell_learning_service()** (3 connections) — `server/game/quest/quest_service.py`
- **.resolve_name_to_quest_id()** (3 connections) — `server/game/quest/quest_service.py`
- **Quest subsystem: service, goal progression, rewards.** (1 connections) — `server/game/quest/__init__.py`
- **Set the spell learning service (e.g. when wired after construction by the contai** (1 connections) — `server/game/quest/quest_service.py`
- **Resolve quest common name to quest_id. Returns None if not found.** (1 connections) — `server/game/quest/quest_service.py`

## Relationships

- [quest game service](quest_game_service.md) (3 shared connections)
- [quest service game](quest_service_game.md) (3 shared connections)

## Source Files

- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*