# Summary E 2 E Remaining

> 8 nodes · cohesion 0.25

## Key Concepts

- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Get appropriate shutdown blocking message for different contexts.      Args:** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns login message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns character creation message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns default message for unknown context** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [Logging Best Practices](Logging_Best_Practices.md) (4 shared connections)
- [Player Effects API](Player_Effects_API.md) (3 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (2 shared connections)
- [Admin Shutdown Commands](Admin_Shutdown_Commands.md) (1 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (1 shared connections)
- [WebSocket Helper Utilities](WebSocket_Helper_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*