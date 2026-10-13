# Community 492

> 36 nodes

## Key Concepts

- **QuestInstanceRepository** (17 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstance** (14 connections) — `server/models/quest.py`
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_start_by_trigger_then_abandon()** (9 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (9 connections) — `server/tests/integration/test_quest_flow.py`
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (7 connections)
- **._fetch_created_quest_row()** (4 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_make_shared_session_factory()** (4 connections) — `server/tests/integration/test_quest_flow.py`
- **mock_quest_instance()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **quest_instance_repository()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Any** (4 connections)
- **.__init__()** (2 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **datetime** (2 connections)
- **asyncio** (2 connections)
- **integration** (2 connections)
- **fixture** (2 connections)
- **Per-character quest state: one row per player per quest.** (1 connections) — `server/models/quest.py`
- **Get the quest instance for this player and quest (any state). Returns None if…** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Update an instance's state and/or progress. Pass only fields to change.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- *... and 11 more nodes in this community*

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (27 shared connections)
- [Community 598](Community_598.md) (4 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 203](Community_203.md) (2 shared connections)
- [Community 674](Community_674.md) (2 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 86 (89%)
- INFERRED: 11 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*