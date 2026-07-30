# look helpers

> 39 nodes

## Key Concepts

- **look_command.py** (37 connections) — `server/commands/look_command.py`
- **Any** (12 connections)
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
- **_route_look_command()** (10 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **handle_look_command()** (8 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (7 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (5 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (5 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (5 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (5 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (4 connections) — `server/commands/look_command.py`
- **test_is_direction_cardinal()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_is_direction_abbreviation()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_is_direction_not_direction()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_is_direction()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_is_direction_false()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **Look command for MythosMUD.  This module handles the look command for examining** (1 connections) — `server/commands/look_command.py`
- **Extract app and persistence from request.** (1 connections) — `server/commands/look_command.py`
- **Validate and retrieve player and room for look command.** (1 connections) — `server/commands/look_command.py`
- **Get room drops from room manager.** (1 connections) — `server/commands/look_command.py`
- **Setup and validate look command prerequisites.** (1 connections) — `server/commands/look_command.py`
- *... and 14 more nodes in this community*

## Relationships

- [look player](look_player.md) (14 shared connections)
- [find container in room or](find_container_in_room_or.md) (5 shared connections)
- [DeathInterstitial](DeathInterstitial.md) (5 shared connections)
- [look room](look_room.md) (5 shared connections)
- [Any](Any.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [test build room drop summary](test_build_room_drop_summary.md) (3 shared connections)
- [Validate that player is in](Validate_that_player_is_in.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [Player Position Service](Player_Position_Service.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_helpers.py`
- `server/tests/unit/commands/test_look_helpers_functions.py`

## Audit Trail

- EXTRACTED: 165 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*