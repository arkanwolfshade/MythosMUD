# Quest Instance Repository

> 27 nodes · cohesion 0.15

## Key Concepts

- **QuestInstanceRepository** (23 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstance** (19 connections) — `server/models/quest.py`
- **quest_instance_repository.py** (14 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.create()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstance** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Any** (5 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **datetime** (4 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **quest_instance_repository()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Per-character quest state: one row per player per quest.** (1 connections) — `server/models/quest.py`
- **Create a QuestInstanceRepository instance.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance repository for quest subsystem.  CRUD for quest_instances via Post** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Get the quest instance for this player and quest (any state). Returns None if no** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Update an instance's state and/or progress. Pass only fields to change.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **List all active quest instances for the player.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **List completed quest instances for the player (for quest log or prerequisite che** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Normalize player_id to string for DB (players.player_id is UUID as_uuid=False).** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Map procedure result row to QuestInstance model.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- *... and 2 more nodes in this community*

## Relationships

- [[NPC Admin API]] (24 shared connections)
- [[Game Service Bundle]] (7 shared connections)
- [[Quest Service Core]] (6 shared connections)
- [[SQLAlchemy Model Base]] (4 shared connections)
- [[Quest Instance Repository Tests]] (3 shared connections)
- [[Quest Flow Integration]] (3 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 127 (83%)
- INFERRED: 26 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
