# QuestInstanceRepository

> 30 nodes

## Key Concepts

- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_start_by_trigger_then_abandon()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (7 connections)
- **._fetch_created_quest_row()** (4 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_make_shared_session_factory()** (4 connections) — `server/tests/integration/test_quest_flow.py`
- **Any** (4 connections)
- **.__init__()** (2 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **integration** (2 connections)
- **datetime** (2 connections)
- **asyncio** (2 connections)
- **serial** (2 connections)
- **Get the quest instance for this player and quest (any state). Returns None if…** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Update an instance's state and/or progress. Pass only fields to change.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **List all active quest instances for the player.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **List completed quest instances for the player (for quest log or prerequisite…** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Normalize player_id to string for DB (players.player_id is UUID as_uuid=False).** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Map procedure result row to QuestInstance model.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- *... and 5 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (24 shared connections)
- [QuestService](QuestService.md) (8 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (2 shared connections)
- [session_factory](session_factory.md) (2 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 77 (88%)
- INFERRED: 11 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*