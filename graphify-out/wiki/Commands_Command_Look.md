# Commands Command Look

> 26 nodes · cohesion 0.11

## Key Concepts

- **Any** (12 connections) — `server/commands/look_command.py`
- **_route_look_command()** (10 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **handle_look_command()** (7 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (7 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (5 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (5 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (5 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (5 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (4 connections) — `server/commands/look_command.py`
- **Setup and validate go command prerequisites.** (2 connections) — `server/commands/go_command.py`
- **Try to handle explicit player look.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit item look.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit container look or container inspection.** (1 connections) — `server/commands/look_command.py`
- **Handle implicit target lookup with priority resolution.** (1 connections) — `server/commands/look_command.py`
- **Try to handle implicit target lookup, returns (result, direction).** (1 connections) — `server/commands/look_command.py`
- **Extract app and persistence from request.** (1 connections) — `server/commands/look_command.py`
- **Try to handle direction look.** (1 connections) — `server/commands/look_command.py`
- **Route look command to appropriate handler.** (1 connections) — `server/commands/look_command.py`
- **Handle the look command for examining surroundings.      Args:         command_d** (1 connections) — `server/commands/look_command.py`
- **Validate and retrieve player and room for look command.** (1 connections) — `server/commands/look_command.py`
- **Get room drops from room manager.** (1 connections) — `server/commands/look_command.py`
- *... and 1 more nodes in this community*

## Relationships

- [[Alias Expansion Logic]] (13 shared connections)
- [[Look Container Command]] (2 shared connections)
- [[Look Item Commands]] (2 shared connections)
- [[Look Player Command]] (2 shared connections)
- [[Room Look Formatting]] (2 shared connections)
- [[Commands Go Command]] (1 shared connections)
- [[Room Drop Renderer]] (1 shared connections)
- [[Look Display Helpers]] (1 shared connections)
- [[Look NPC Command]] (1 shared connections)
- [[Command Helper Utilities]] (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/commands/look_command.py`

## Audit Trail

- EXTRACTED: 97 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
