# quest_service

> 7 nodes

## Key Concepts

- **quest_service()** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **mock_def_repo()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **mock_instance_repo()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **fixture** (3 connections)
- **Mock QuestDefinitionRepository.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **Mock QuestInstanceRepository.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **QuestService with mocked repos.** (1 connections) — `server/tests/unit/game/test_quest_service.py`

## Relationships

- [test_quest_service.py](test_quest_service.py.md) (3 shared connections)
- [QuestService](QuestService.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)
- [quest_commands.py](quest_commands.py.md) (1 shared connections)
- [quest_events.py](quest_events.py.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 10 (67%)
- INFERRED: 5 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*