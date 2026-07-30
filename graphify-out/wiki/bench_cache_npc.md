# bench cache npc

> 97 nodes

## Key Concepts

- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstanceRepository** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **quest.py** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.get_by_player_and_quest()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (8 connections)
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_start_log_abandon_flow()** (7 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_by_trigger_then_abandon()** (7 connections) — `server/tests/integration/test_quest_flow.py`
- **QuestOffer** (6 connections) — `server/models/quest.py`
- **_row_for_quest_instance()** (6 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_make_shared_session_factory()** (5 connections) — `server/tests/integration/test_quest_flow.py`
- **Any** (4 connections)
- **_row_for_quest_definition()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_success()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- *... and 72 more nodes in this community*

## Relationships

- [real time](real_time.md) (49 shared connections)
- [QuestCompleted](QuestCompleted.md) (11 shared connections)
- [main()](main%28%29.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [metrics](metrics.md) (1 shared connections)
- [test command factories communication](test_command_factories_communication.md) (1 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 371 (93%)
- INFERRED: 26 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*