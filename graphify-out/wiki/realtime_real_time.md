# realtime real time

> 174 nodes

## Key Concepts

- **command_service.py** (95 connections) — `server/commands/command_service.py`
- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **lucidity_recovery_commands.py** (25 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **handle_pray_command()** (21 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionOnCooldownError** (18 connections) — `server/services/active_lucidity_service.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **_perform_recovery_action()** (15 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pose_command()** (13 connections) — `server/commands/communication_commands.py`
- **handle_inventory_command()** (13 connections) — `server/commands/inventory_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_unalias_command()** (12 connections) — `server/commands/alias_commands.py`
- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **handle_aliases_command()** (11 connections) — `server/commands/alias_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **handle_meditate_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (8 connections)
- **handle_therapy_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **_create_alias()** (5 connections) — `server/commands/alias_commands.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- *... and 149 more nodes in this community*

## Relationships

- [alias storage rationale](alias_storage_rationale.md) (24 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (15 shared connections)
- [commands whisper command](commands_whisper_command.md) (14 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (11 shared connections)
- [commands admin mute](commands_admin_mute.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (10 shared connections)
- [position player service](position_player_service.md) (8 shared connections)
- [commands communication flows](commands_communication_flows.md) (5 shared connections)
- [game models player](game_models_player.md) (5 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (4 shared connections)
- [command factories create](command_factories_create.md) (4 shared connections)
- [commands position system](commands_position_system.md) (4 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/alias_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/lucidity_recovery_commands.py`
- `server/commands/system_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_alias_commands.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 720 (98%)
- INFERRED: 15 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*