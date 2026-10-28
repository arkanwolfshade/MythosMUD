# ErrorContext

> 130 nodes · cohesion 0.03

## Key Concepts

- **admin_teleport_commands.py** (37 connections) — `server/commands/admin_teleport_commands.py`
- **test_teleport_helpers.py** (31 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **teleport_helpers.py** (28 connections) — `server/commands/teleport_helpers.py`
- **admin_teleport_utils.py** (24 connections) — `server/commands/admin_teleport_utils.py`
- **broadcast_teleport_effects()** (21 connections) — `server/commands/admin_teleport_utils.py`
- **notify_player_of_teleport()** (21 connections) — `server/commands/admin_teleport_utils.py`
- **test_admin_commands_helpers.py** (20 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_admin_teleport_utils.py** (18 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **create_teleport_effect_message()** (16 connections) — `server/commands/admin_teleport_utils.py`
- **get_online_player_by_display_name()** (15 connections) — `server/commands/admin_teleport_utils.py`
- **asyncio** (12 connections)
- **_execute_teleport_move()** (11 connections) — `server/commands/admin_teleport_commands.py`
- **execute_confirm_teleport()** (10 connections) — `server/commands/teleport_helpers.py`
- **Any** (10 connections)
- **resolve_target_player()** (10 connections) — `server/commands/teleport_helpers.py`
- **update_player_room_location()** (10 connections) — `server/commands/teleport_helpers.py`
- **update_teleport_location()** (10 connections) — `server/commands/teleport_helpers.py`
- **asyncio** (10 connections)
- **_resolve_teleport_execution_context()** (9 connections) — `server/commands/admin_teleport_commands.py`
- **broadcast_teleport_updates()** (9 connections) — `server/commands/teleport_helpers.py`
- **resolve_target_player_for_teleport()** (9 connections) — `server/commands/teleport_helpers.py`
- **resolve_teleport_direction()** (9 connections) — `server/commands/teleport_helpers.py`
- **resolve_teleport_services()** (9 connections) — `server/commands/teleport_helpers.py`
- **validate_confirm_teleport_context()** (9 connections) — `server/commands/teleport_helpers.py`
- **_announce_confirm_teleport()** (7 connections) — `server/commands/teleport_helpers.py`
- *... and 105 more nodes in this community*

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (20 shared connections)
- [Async Code Review - Post Phase 2 Migration](Async_Code_Review_-_Post_Phase_2_Migration.md) (18 shared connections)
- [command_parser.py](command_parser.py.md) (17 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (11 shared connections)
- [Room](Room.md) (6 shared connections)
- [look_container.py](look_container.py.md) (5 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (5 shared connections)
- [.publish_with_pool](publish_with_pool.md) (4 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (2 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (1 shared connections)

## Source Files

- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/teleport_helpers.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`
- `server/tests/unit/commands/test_admin_teleport_utils.py`
- `server/tests/unit/commands/test_teleport_helpers.py`

## Audit Trail

- EXTRACTED: 347 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*