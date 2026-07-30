# notify quest abandoned()

> 4 nodes

## Key Concepts

- **quest_service()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **_collect_progress_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **Return quest_service.sync_collect_progress when it is callable.** (1 connections) — `server/commands/inventory_command_helpers.py`
- **QuestService with mocked repos.** (1 connections) — `server/tests/unit/game/test_quest_service.py`

## Relationships

- [Any](Any.md) (3 shared connections)
- [QuestCompleted](QuestCompleted.md) (2 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (1 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [test quest service](test_quest_service.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 8 (53%)
- INFERRED: 7 (47%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*