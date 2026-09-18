# Community 442

> 40 nodes

## Key Concepts

- **get_username_from_user()** (51 connections) — `server/utils/command_helpers.py`
- **.async_persistence()** (27 connections) — `server/commands/cleanse_command.py`
- **follow_commands.py** (18 connections) — `server/commands/follow_commands.py`
- **handle_following_command()** (10 connections) — `server/commands/follow_commands.py`
- **handle_unfollow_command()** (10 connections) — `server/commands/follow_commands.py`
- **._get_persistence_from_app()** (6 connections) — `server/commands/combat_handler.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **_get_container()** (6 connections) — `server/commands/follow_commands.py`
- **_load_follow_context()** (6 connections) — `server/commands/follow_commands.py`
- **Any** (6 connections)
- **_resolve_follow_target()** (4 connections) — `server/commands/follow_commands.py`
- **test_get_username_from_user_empty_dict()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_none()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_name_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_player_object()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_priority_player_over_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_username_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **_username_from_dict()** (3 connections) — `server/utils/command_helpers.py`
- **AppWithState** (3 connections)
- **Get player data and room, returning error dict if any step fails. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Resolve persistence from app (container preferred, then app.state). Returns…** (1 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails.** (1 connections) — `server/commands/combat_handler.py`
- *... and 15 more nodes in this community*

## Relationships

- [Community 495](Community_495.md) (13 shared connections)
- [Community 865](Community_865.md) (12 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (6 shared connections)
- [Community 44](Community_44.md) (4 shared connections)
- [Community 471](Community_471.md) (4 shared connections)
- [Community 626](Community_626.md) (3 shared connections)
- [Community 135](Community_135.md) (3 shared connections)
- [Community 89](Community_89.md) (3 shared connections)
- [Community 25](Community_25.md) (3 shared connections)
- [Community 32](Community_32.md) (3 shared connections)
- [Community 433](Community_433.md) (3 shared connections)
- [Community 514](Community_514.md) (2 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/commands/combat_handler.py`
- `server/commands/follow_commands.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 92 (60%)
- INFERRED: 61 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*