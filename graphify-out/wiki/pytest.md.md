# pytest.md

> 263 nodes

## Key Concepts

- **command_service.py** (108 connections) — `server/commands/command_service.py`
- **get_username_from_user()** (45 connections) — `server/utils/command_helpers.py`
- **admin_teleport_commands.py** (39 connections) — `server/commands/admin_teleport_commands.py`
- **admin_summon_command.py** (35 connections) — `server/commands/admin_summon_command.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **test_teleport_helpers.py** (32 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **get_admin_actions_logger()** (27 connections) — `server/structured_logging/admin_actions_logger.py`
- **teleport_helpers.py** (24 connections) — `server/commands/teleport_helpers.py`
- **admin_actions_logger.py** (19 connections) — `server/structured_logging/admin_actions_logger.py`
- **handle_mute_command()** (18 connections) — `server/commands/admin_mute_commands.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Any** (16 connections)
- **handle_inventory_command()** (13 connections) — `server/commands/inventory_commands.py`
- **get_help_content()** (13 connections) — `server/help/help_content.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **help_content.py** (12 connections) — `server/help/help_content.py`
- **asyncio** (12 connections)
- **handle_mutes_command()** (11 connections) — `server/commands/admin_mute_commands.py`
- **handle_unmute_command()** (11 connections) — `server/commands/admin_mute_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **execute_confirm_teleport()** (11 connections) — `server/commands/teleport_helpers.py`
- *... and 238 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (79 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (31 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (22 shared connections)
- [ContainerComponent](ContainerComponent.md) (18 shared connections)
- [CombatParticipant](CombatParticipant.md) (17 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (17 shared connections)
- [RoomService](RoomService.md) (14 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (13 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (11 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (9 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (8 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (7 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/admin_permission_utils.py`
- `server/commands/admin_setstat_command.py`
- `server/commands/admin_summon_command.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/command_service.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/system_commands.py`
- `server/commands/teleport_helpers.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/structured_logging/log_time_formats.py`
- `server/tests/unit/commands/test_admin_commands.py`
- `server/tests/unit/commands/test_exploration_commands.py`
- `server/tests/unit/commands/test_help_commands.py`

## Audit Trail

- EXTRACTED: 712 (86%)
- INFERRED: 118 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*