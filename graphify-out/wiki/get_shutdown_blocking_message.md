# get_shutdown_blocking_message

> 8 nodes

## Key Concepts

- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Get appropriate shutdown blocking message for different contexts. Args:…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns login message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns character creation message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns default message for unknown…** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (4 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [register_user](register_user.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*