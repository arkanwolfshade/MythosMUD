# commands follow rationale

> 6 nodes

## Key Concepts

- **.create_quest_command()** (5 connections) — `server/utils/command_factories_player_state.py`
- **test_create_quest_command_empty_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_quest_command_with_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **Test create_quest_command() with no args creates QuestCommand with empty list.** (1 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **Test create_quest_command() with args passes them to QuestCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **Create QuestCommand from arguments (e.g. abandon <quest name>).** (1 connections) — `server/utils/command_factories_player_state.py`

## Relationships

- [add used user](add_used_user.md) (2 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_player_state.py`
- `server/utils/command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*