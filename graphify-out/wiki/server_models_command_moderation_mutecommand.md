# server models command moderation mutecommand

> 84 nodes

## Key Concepts

- **ModerationCommandFactory** (37 connections) — `server/utils/command_factories_moderation.py`
- **test_command_factories_moderation.py** (30 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **.create_mute_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_mute_global_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_add_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_global_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_mutes_command()** (6 connections) — `server/utils/command_factories_moderation.py`
- **test_create_add_admin_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_add_admin_command_with_multiple_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_admin_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_admin_command_status_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_mute_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_mute_global_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_mutes_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_unmute_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_unmute_command_with_multiple_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_unmute_global_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_unmute_global_command_with_multiple_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_add_admin_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_admin_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_create_mute_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- *... and 59 more nodes in this community*

## Relationships

- [claude rules pydantic](claude_rules_pydantic.md) (20 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (13 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (8 shared connections)
- [server models command base basecommand](server_models_command_base_basecommand.md) (4 shared connections)
- [server models command alias aliascommand](server_models_command_alias_aliascommand.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [server monitoring exception metrics](server_monitoring_exception_metrics.md) (1 shared connections)

## Source Files

- `server/models/command_moderation.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/utils/command_factories_moderation.py`

## Audit Trail

- EXTRACTED: 153 (81%)
- INFERRED: 37 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*