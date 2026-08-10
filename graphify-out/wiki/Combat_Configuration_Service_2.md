# Combat Configuration Service

> 46 nodes

## Key Concepts

- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_utility.py** (18 connections) — `server/models/command_utility.py`
- **HelpCommand** (13 connections) — `server/models/command_utility.py`
- **WhoCommand** (13 connections) — `server/models/command_utility.py`
- **StatusCommand** (8 connections) — `server/models/command_utility.py`
- **TimeCommand** (8 connections) — `server/models/command_utility.py`
- **WhoamiCommand** (8 connections) — `server/models/command_utility.py`
- **.create_help_command()** (5 connections) — `server/utils/command_factories_utility.py`
- **test_help_command_topic_max_length()** (4 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_who_command_filter_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_help_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_help_command_with_topic()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_help_command_validate_topic_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_help_command_validate_topic_none()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_who_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_who_command_with_filter_name()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_who_command_validate_filter_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_who_command_validate_filter_name_none()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_status_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_time_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_whoami_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_utility.py`
- **test_create_help_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_help_command_no_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Utility command models for MythosMUD.  This module provides command models for u** (1 connections) — `server/models/command_utility.py`
- **Command for getting help on commands.** (1 connections) — `server/models/command_utility.py`
- *... and 21 more nodes in this community*

## Relationships

- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (8 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (7 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (6 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (5 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (5 shared connections)

## Source Files

- `server/models/command_utility.py`
- `server/tests/unit/models/test_command_utility.py`
- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 151 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*