# Test Admin Shutdown Command

> 8 nodes

## Key Concepts

- **get_shutdown_blocking_message()** (9 connections) — `server/commands/admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Get appropriate shutdown blocking message for different contexts. Args:…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns login message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns character creation message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns default message for unknown…** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [Test Admin Shutdown Command](Test_Admin_Shutdown_Command.md) (4 shared connections)
- [Character Creation API](Character_Creation_API.md) (3 shared connections)
- [Admin Shutdown Command](Admin_Shutdown_Command.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*