# QuestInstance

> 30 nodes

## Key Concepts

- **QuestInstance** (21 connections) — `server/models/quest.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **quest_instance_repository.py** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (7 connections)
- **._fetch_created_quest_row()** (4 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **mock_quest_instance()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **quest_instance_repository()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Any** (4 connections)
- **.__init__()** (2 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **datetime** (2 connections)
- **fixture** (2 connections)
- **Per-character quest state: one row per player per quest.** (1 connections) — `server/models/quest.py`
- **QuestInstance repository for quest subsystem. CRUD for quest_instances via…** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Get the quest instance for this player and quest (any state). Returns None if…** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Update an instance's state and/or progress. Pass only fields to change.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **List all active quest instances for the player.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **List completed quest instances for the player (for quest log or prerequisite…** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Normalize player_id to string for DB (players.player_id is UUID as_uuid=False).** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- *... and 5 more nodes in this community*

## Relationships

- [get_session_maker](get_session_maker.md) (15 shared connections)
- [DatabaseError](DatabaseError.md) (9 shared connections)
- [QuestService](QuestService.md) (7 shared connections)
- [log_and_raise](log_and_raise.md) (7 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (2 shared connections)
- [._init_player_quest_layer](_init_player_quest_layer.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 93 (90%)
- INFERRED: 10 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*