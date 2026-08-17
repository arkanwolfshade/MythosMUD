# PlayerCombatState

> 14 nodes

## Key Concepts

- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **test_get_player_combat_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end_clears_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_is_player_in_combat_sync_true()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_combat_state_post_init()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_combat_state_post_init_with_activity()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.__post_init__()** (2 connections) — `server/services/player_combat_service.py`
- **Represents a player's combat state.** (1 connections) — `server/services/player_combat_service.py`
- **Initialize last_activity if not provided.** (1 connections) — `server/services/player_combat_service.py`
- **Test is_player_in_combat_sync returns True when in combat.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test handle_combat_end clears player combat state.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test PlayerCombatState.__post_init__ sets last_activity.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test PlayerCombatState.__post_init__ preserves provided last_activity.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test get_player_combat_state returns state.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`

## Relationships

- [test_player_combat_service.py](test_player_combat_service.py.md) (11 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [UUID](UUID.md) (2 shared connections)

## Source Files

- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 19 (63%)
- INFERRED: 11 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*