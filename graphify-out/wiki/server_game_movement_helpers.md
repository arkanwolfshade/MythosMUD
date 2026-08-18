# server game movement helpers

> 27 nodes

## Key Concepts

- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **test_check_combat_state_allows_without_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_blocks_when_in_combat()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_player_posture_blocks_sitting()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_exit_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_exit_no_exits()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_exit_target_missing_in_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **Room** (2 connections)
- **Movement validation helpers for MovementService. Cohesive validation and room-…** (1 connections) — `server/game/movement_helpers.py`
- **Validate player is in the from_room, auto-adding if database matches.** (1 connections) — `server/game/movement_helpers.py`
- **Validate that there's a valid exit from the room to the target room.** (1 connections) — `server/game/movement_helpers.py`
- **Extract and validate player ID from player object.** (1 connections) — `server/game/movement_helpers.py`
- **Check if player is in combat (blocks movement).** (1 connections) — `server/game/movement_helpers.py`
- **Check if player posture allows movement (only standing allowed).** (1 connections) — `server/game/movement_helpers.py`
- **Test check_combat_state returns False when player is in combat.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test check_combat_state allows movement when no combat service.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test check_player_posture blocks non-standing posture.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test validate_exit returns False when room has no exits.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [server tests unit game test](server_tests_unit_game_test.md) (13 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (5 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (3 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [server models room py any](server_models_room_py_any.md) (1 shared connections)
- [server async persistence](server_async_persistence.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 70 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*