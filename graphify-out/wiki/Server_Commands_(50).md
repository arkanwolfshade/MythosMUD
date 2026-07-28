# Server Commands (50)

> 23 nodes

## Key Concepts

- **Any** (12 connections)
- **_route_look_command()** (10 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (7 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (5 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (5 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (5 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (5 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (4 connections) — `server/commands/look_command.py`
- **Extract app and persistence from request.** (1 connections) — `server/commands/look_command.py`
- **Validate and retrieve player and room for look command.** (1 connections) — `server/commands/look_command.py`
- **Get room drops from room manager.** (1 connections) — `server/commands/look_command.py`
- **Setup and validate look command prerequisites.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit player look.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit item look.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit container look or container inspection.** (1 connections) — `server/commands/look_command.py`
- **Handle implicit target lookup with priority resolution.** (1 connections) — `server/commands/look_command.py`
- **Try to handle implicit target lookup, returns (result, direction).** (1 connections) — `server/commands/look_command.py`
- **Try to handle direction look.** (1 connections) — `server/commands/look_command.py`
- **Route look command to appropriate handler.** (1 connections) — `server/commands/look_command.py`

## Relationships

- [Server Commands](Server_Commands.md) (14 shared connections)
- [Server Commands (17)](Server_Commands_%2817%29.md) (2 shared connections)
- [Server Commands (41)](Server_Commands_%2841%29.md) (2 shared connections)
- [Server Commands (12)](Server_Commands_%2812%29.md) (2 shared connections)
- [Server Commands (13)](Server_Commands_%2813%29.md) (2 shared connections)
- [Server Utils (6)](Server_Utils_%286%29.md) (1 shared connections)
- [Server Utils (8)](Server_Utils_%288%29.md) (1 shared connections)
- [Server Commands (11)](Server_Commands_%2811%29.md) (1 shared connections)
- [Server Commands (22)](Server_Commands_%2822%29.md) (1 shared connections)

## Source Files

- `server/commands/look_command.py`

## Audit Trail

- EXTRACTED: 87 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*