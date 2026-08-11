# Persistence Extraction Complete

> 16 nodes

## Key Concepts

- **get_help_content()** (14 connections) — `server/help/help_content.py`
- **test_websocket_handler_help.py** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **__init__.py** (3 connections) — `server/help/__init__.py`
- **_get_general_help()** (3 connections) — `server/help/help_content.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_general()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_specific()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **Help system for MythosMUD.  This package provides help content and command docum** (1 connections) — `server/help/__init__.py`
- **Get help content for commands.      Args:         command_name: Optional specifi** (1 connections) — `server/help/help_content.py`
- **Get general help content with command categories.** (1 connections) — `server/help/help_content.py`
- **Test get_help_content returns help content.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test get_help_content returns help for specific command.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Unit tests for help content used in the realtime/WebSocket path.  Uses the canon** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **Test get_help_content() returns general help when no command specified.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **Test get_help_content() returns specific command help for look.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (3 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (2 shared connections)
- [Container Open Events](Container_Open_Events.md) (2 shared connections)

## Source Files

- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*