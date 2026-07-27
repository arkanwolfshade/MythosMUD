# Alias Expansion Logic

> 403 nodes · cohesion 0.01

## Key Concepts

- **AliasStorage** (132 connections) — `server/alias_storage.py`
- **command_service.py** (91 connections) — `server/commands/command_service.py`
- **alias_storage.py** (64 connections) — `server/alias_storage.py`
- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **command_parser.py** (38 connections) — `server/utils/command_parser.py`
- **look_command.py** (37 connections) — `server/commands/look_command.py`
- **admin_commands.py** (32 connections) — `server/commands/admin_commands.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **rescue_commands.py** (29 connections) — `server/commands/rescue_commands.py`
- **test_alias_commands.py** (29 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **go_command.py** (27 connections) — `server/commands/go_command.py`
- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **party_commands.py** (19 connections) — `server/commands/party_commands.py`
- **handle_mute_command()** (18 connections) — `server/commands/admin_mute_commands.py`
- **logout_commands.py** (18 connections) — `server/commands/logout_commands.py`
- **utility_commands.py** (18 connections) — `server/commands/utility_commands.py`
- **AliasGraph** (18 connections) — `server/utils/alias_graph.py`
- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **position_commands.py** (17 connections) — `server/commands/position_commands.py`
- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **handle_debrief_command()** (16 connections) — `server/commands/debrief_command.py`
- *... and 378 more nodes in this community*

## Relationships

- [[NPC Admin API]] (105 shared connections)
- [[Combat Command Handler]] (44 shared connections)
- [[Admin Status Commands]] (26 shared connections)
- [[Admin Summon Command]] (25 shared connections)
- [[Unified Command Handler]] (19 shared connections)
- [[Ground and Rescue Commands]] (15 shared connections)
- [[Commands Command Look]] (13 shared connections)
- [[Command Input Utilities]] (12 shared connections)
- [[NPC Admin Commands]] (12 shared connections)
- [[Commands Go Command]] (12 shared connections)
- [[Communication Command Handlers]] (11 shared connections)
- [[Magic Command Handlers]] (11 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/processing.py`
- `server/command_handler_unified.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/alias_commands.py`
- `server/commands/channel_commands.py`
- `server/commands/command_service.py`
- `server/commands/debrief_command.py`
- `server/commands/emote_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/follow_commands.py`
- `server/commands/go_command.py`
- `server/commands/logout_commands.py`
- `server/commands/look_command.py`
- `server/commands/npc_admin/behavior.py`

## Audit Trail

- EXTRACTED: 1962 (96%)
- INFERRED: 91 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
