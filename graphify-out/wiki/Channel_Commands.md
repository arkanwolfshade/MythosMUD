# Channel Commands

> 188 nodes

## Key Concepts

- **command_parser.py** (52 connections) — `server/utils/command_parser.py`
- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_command_helpers.py** (21 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_command_parser_helpers.py** (21 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_channel_commands.py** (20 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **channel_commands.py** (17 connections) — `server/commands/channel_commands.py`
- **skills_commands.py** (16 connections) — `server/commands/skills_commands.py`
- **command_helpers.py** (16 connections) — `server/utils/command_helpers.py`
- **handle_channel_command()** (13 connections) — `server/commands/channel_commands.py`
- **test_command_helpers_functions.py** (13 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **handle_skills_command()** (12 connections) — `server/commands/skills_commands.py`
- **test_skills_commands.py** (11 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **_handle_default_channel_setting()** (10 connections) — `server/commands/channel_commands.py`
- **_perform_recovery_action()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (10 connections)
- **_run_recovery_session()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **asyncio** (9 connections)
- **_extract_channel_from_command()** (8 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (8 connections) — `server/commands/channel_commands.py`
- **handle_group_solace_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **_get_container_services()** (8 connections) — `server/commands/skills_commands.py`
- **handle_therapy_command()** (7 connections) — `server/commands/lucidity_recovery_commands.py`
- **_resolve_player_id()** (7 connections) — `server/commands/skills_commands.py`
- *... and 163 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (30 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (19 shared connections)
- [Community 122](Community_122.md) (15 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (8 shared connections)
- [Assist Wiring Tests](Assist_Wiring_Tests.md) (8 shared connections)
- [Community 42](Community_42.md) (6 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (6 shared connections)
- [Character Creation & Professions](Character_Creation_&_Professions.md) (4 shared connections)
- [Base Command Models](Base_Command_Models.md) (4 shared connections)
- [Community 187](Community_187.md) (3 shared connections)
- [Community 242](Community_242.md) (3 shared connections)
- [Community 468](Community_468.md) (3 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/commands/lucidity_recovery_commands.py`
- `server/commands/skills_commands.py`
- `server/tests/unit/commands/test_channel_commands.py`
- `server/tests/unit/commands/test_skills_commands.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/utils/command_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 395 (90%)
- INFERRED: 45 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*