# Client Event Store

> 706 nodes

## Key Concepts

- **AliasStorage** (230 connections) — `server/alias_storage.py`
- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **alias_storage.py** (64 connections) — `server/alias_storage.py`
- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **command_parser.py** (45 connections) — `server/utils/command_parser.py`
- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_admin_commands.py** (37 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **handle_alias_command()** (25 connections) — `server/commands/alias_commands.py`
- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **ActiveLucidityService** (24 connections) — `server/services/active_lucidity_service.py`
- **handle_pray_command()** (22 connections) — `server/commands/lucidity_recovery_commands.py`
- *... and 681 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (89 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (34 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (31 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (28 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (26 shared connections)
- [Player Death Service](Player_Death_Service.md) (20 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (17 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (17 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (17 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (17 shared connections)
- [WebSocket Handler Helpers](WebSocket_Handler_Helpers.md) (16 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (14 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/processing.py`
- `server/command_handler_unified.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/alias_commands.py`
- `server/commands/channel_commands.py`
- `server/commands/combat_handler.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/debrief_command.py`
- `server/commands/exploration_commands.py`
- `server/commands/follow_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 3189 (92%)
- INFERRED: 272 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*