# Container Open Events

> 448 nodes

## Key Concepts

- **AliasStorage** (230 connections) — `server/alias_storage.py`
- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **alias_storage.py** (64 connections) — `server/alias_storage.py`
- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **command_parser.py** (45 connections) — `server/utils/command_parser.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **handle_alias_command()** (25 connections) — `server/commands/alias_commands.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **ActiveLucidityService** (24 connections) — `server/services/active_lucidity_service.py`
- **handle_pray_command()** (22 connections) — `server/commands/lucidity_recovery_commands.py`
- **position_commands.py** (21 connections) — `server/commands/position_commands.py`
- **handle_mute_command()** (20 connections) — `server/commands/admin_mute_commands.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **Any** (20 connections)
- **combat.py** (19 connections) — `server/commands/combat.py`
- *... and 423 more nodes in this community*

## Relationships

- [Chat NATS Publisher](Chat_NATS_Publisher.md) (41 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (37 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (36 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (32 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (32 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (31 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (27 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (23 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (22 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (21 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (21 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (20 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/command_handler/alias_expansion.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/alias_commands.py`
- `server/commands/channel_commands.py`
- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/debrief_command.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/lucidity_recovery_commands.py`
- `server/commands/magic_commands.py`
- `server/commands/position_commands.py`
- `server/commands/skills_commands.py`
- `server/commands/system_commands.py`

## Audit Trail

- EXTRACTED: 2200 (90%)
- INFERRED: 234 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*