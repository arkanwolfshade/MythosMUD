# UpgradeImplementationPlan

> 18 nodes · cohesion 0.11

## Key Concepts

- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **test_cleanup_stale_combat_states()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state_not_found()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start_tracks_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_is_player_in_combat_sync_true()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_combat_state_post_init()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_combat_state_post_init_with_activity()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.__post_init__()** (2 connections) — `server/services/player_combat_service.py`
- **Represents a player's combat state.** (1 connections) — `server/services/player_combat_service.py`
- **Initialize last_activity if not provided.** (1 connections) — `server/services/player_combat_service.py`
- **Test get_player_combat_state returns None when not found.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test is_player_in_combat_sync returns True when in combat.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test cleanup_stale_combat_states cleans up stale states.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test handle_combat_start tracks player combat state.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test PlayerCombatState.__post_init__ sets last_activity.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test PlayerCombatState.__post_init__ preserves provided last_activity.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test get_player_combat_state returns state.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`

## Relationships

- [CharacterNameScreen.tsx](CharacterNameScreen.tsx.md) (13 shared connections)
- [validate_secure_path](validate_secure_path.md) (5 shared connections)
- [The Toolkit](The_Toolkit.md) (2 shared connections)
- [_MigrationArgs](_MigrationArgs.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 28 (74%)
- INFERRED: 10 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*