# quest_service

> 9 nodes

## Key Concepts

- **quest_service()** (11 connections) — `server/tests/unit/game/test_quest_service.py`
- **_collect_progress_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **mock_def_repo()** (4 connections) — `server/tests/unit/game/test_quest_service.py`
- **mock_instance_repo()** (4 connections) — `server/tests/unit/game/test_quest_service.py`
- **fixture** (3 connections)
- **Return quest_service.sync_collect_progress when it is callable.** (1 connections) — `server/commands/inventory_command_helpers.py`
- **QuestService with mocked repos.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **Mock QuestDefinitionRepository.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **Mock QuestInstanceRepository.** (1 connections) — `server/tests/unit/game/test_quest_service.py`

## Relationships

- [test_quest_service.py](test_quest_service.py.md) (7 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [QuestService](QuestService.md) (2 shared connections)
- [quest_commands.py](quest_commands.py.md) (1 shared connections)
- [NPCDied](NPCDied.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 16 (70%)
- INFERRED: 7 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*