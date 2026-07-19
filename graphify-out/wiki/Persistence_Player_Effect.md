# Persistence Player Effect

> 25 nodes · cohesion 0.10

## Key Concepts

- **test_player_effect_repository.py** (15 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_make_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_row_from_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_active_effects_for_player_filters_by_remaining()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_true()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_add_effect_returns_id()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_delete_effect()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_expire_effects_for_tick_returns_expired_and_deletes()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks_none()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_false()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **player_id()** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Unit tests for PlayerEffectRepository (ADR-009 effects system).  Tests add_effec** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_active_effects_for_player returns only effects with remaining_ticks > 0 (pro** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **has_effect returns True when player has active effect of type.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **has_effect returns False when no active effect of type.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_effect_remaining_ticks returns duration - (current_tick - applied_at_tick).** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_effect_remaining_ticks returns None when no matching effect.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **expire_effects_for_tick returns (player_id, effect_type) and deletes rows via pr** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Create PlayerEffectRepository instance.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Build a mock PlayerEffect with given fields.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Build a procedure result row (mappings().all() item) from effect mock.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **add_effect persists effect and returns effect id (via add_player_effect procedur** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **delete_effect removes effect by id.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`

## Relationships

- [[NPC Admin API]] (2 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
