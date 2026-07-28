# Look Item Command Tests

> 19 nodes · cohesion 0.13

## Key Concepts

- **get_help_content()** (14 connections) — `server/help/help_content.py`
- **help_content.py** (12 connections) — `server/help/help_content.py`
- **test_websocket_handler_help.py** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **get_commands_by_category()** (3 connections) — `server/help/help_content.py`
- **_get_general_help()** (3 connections) — `server/help/help_content.py`
- **__init__.py** (3 connections) — `server/help/__init__.py`
- **test_get_help_content_general()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_specific()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **get_command_categories()** (2 connections) — `server/help/help_content.py`
- **Any** (1 connections)
- **Help content and command documentation for MythosMUD.  This module contains the** (1 connections) — `server/help/help_content.py`
- **Get help content for commands.      Args:         command_name: Optional specifi** (1 connections) — `server/help/help_content.py`
- **Get general help content with command categories.** (1 connections) — `server/help/help_content.py`
- **Get list of all command categories.** (1 connections) — `server/help/help_content.py`
- **Get all commands in a specific category.** (1 connections) — `server/help/help_content.py`
- **Help system for MythosMUD.  This package provides help content and command docum** (1 connections) — `server/help/__init__.py`
- **Unit tests for help content used in the realtime/WebSocket path.  Uses the canon** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **Test get_help_content() returns general help when no command specified.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **Test get_help_content() returns specific command help for look.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`

## Relationships

- [Database Manager Tests](Database_Manager_Tests.md) (4 shared connections)
- [Command Request App State](Command_Request_App_State.md) (3 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)

## Source Files

- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*