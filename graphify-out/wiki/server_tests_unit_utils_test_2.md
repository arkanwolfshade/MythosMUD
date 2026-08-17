# server tests unit utils test

> 72 nodes

## Key Concepts

- **PlayerStateCommandFactory** (40 connections) — `server/utils/command_factories_player_state.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **.create_journal_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_quests_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_quit_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_rest_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_skills_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_status_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_time_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_whoami_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **test_create_journal_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_quests_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_quit_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_rest_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_skills_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_status_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_time_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_whoami_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **.create_logout_command()** (5 connections) — `server/utils/command_factories_player_state.py`
- **.create_quest_command()** (5 connections) — `server/utils/command_factories_player_state.py`
- **.create_who_command()** (5 connections) — `server/utils/command_factories_player_state.py`
- **test_create_journal_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_logout_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_logout_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_quest_command_empty_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- *... and 47 more nodes in this community*

## Relationships

- [characterinfo](characterinfo.md) (23 shared connections)
- [server models command](server_models_command.md) (12 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (10 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (9 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (6 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_player_state.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 123 (80%)
- INFERRED: 31 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*