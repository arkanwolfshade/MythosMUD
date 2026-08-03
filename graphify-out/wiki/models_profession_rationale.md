# models profession rationale

> 8 nodes

## Key Concepts

- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Get appropriate shutdown blocking message for different contexts.      Args:** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns login message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns character creation message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns default message for unknown context** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [shutdown admin command](shutdown_admin_command.md) (5 shared connections)
- [profession game service](profession_game_service.md) (2 shared connections)
- [game models stats](game_models_stats.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*