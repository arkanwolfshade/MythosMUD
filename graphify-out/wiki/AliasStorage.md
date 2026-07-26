# AliasStorage

> 233 nodes · cohesion 0.02

## Key Concepts

- **AliasStorage** (230 connections) — `server/alias_storage.py`
- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **alias_storage.py** (64 connections) — `server/alias_storage.py`
- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **admin_setlucidity_command.py** (28 connections) — `server/commands/admin_setlucidity_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **lucidity_recovery_commands.py** (25 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_mute_command()** (20 connections) — `server/commands/admin_mute_commands.py`
- **Any** (20 connections)
- **position_commands.py** (19 connections) — `server/commands/position_commands.py`
- **Any** (16 connections)
- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_admin_command()** (14 connections) — `server/commands/admin_commands.py`
- **handle_inventory_command()** (14 connections) — `server/commands/inventory_commands.py`
- **handle_unmute_command()** (13 connections) — `server/commands/admin_mute_commands.py`
- **handle_unalias_command()** (13 connections) — `server/commands/alias_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_add_admin_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- *... and 208 more nodes in this community*

## Relationships

- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (34 shared connections)
- [get_logger](get_logger.md) (32 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (32 shared connections)
- [router.py](router.py.md) (32 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (29 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (28 shared connections)
- [SchemaValidator](SchemaValidator.md) (22 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (22 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (22 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (17 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (16 shared connections)
- [__init__.py](__init__.py.md) (16 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/admin_setlucidity_command.py`
- `server/commands/admin_summon_command.py`
- `server/commands/alias_commands.py`
- `server/commands/channel_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/lucidity_recovery_commands.py`
- `server/commands/magic_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 1451 (89%)
- INFERRED: 184 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*