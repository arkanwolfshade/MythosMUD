# test_player_effect_repository.py

> 27 nodes

## Key Concepts

- **test_player_effect_repository.py** (18 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **asyncio** (8 connections)
- **_make_effect()** (6 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_row_from_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_active_effects_for_player_filters_by_remaining()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_true()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **repo()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_add_effect_returns_id()** (3 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_delete_effect()** (3 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_expire_effects_for_tick_returns_expired_and_deletes()** (3 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks_none()** (3 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_false()** (3 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **player_id()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **fixture** (2 connections)
- **Unit tests for PlayerEffectRepository (ADR-009 effects system). Tests…** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_active_effects_for_player returns only effects with remaining_ticks > 0…** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **has_effect returns True when player has active effect of type.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **has_effect returns False when no active effect of type.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_effect_remaining_ticks returns duration - (current_tick - applied_at_tick).** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_effect_remaining_ticks returns None when no matching effect.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **expire_effects_for_tick returns (player_id, effect_type) and deletes rows via…** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Create PlayerEffectRepository instance.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Build a mock PlayerEffect with given fields.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Build a procedure result row (mappings().all() item) from effect mock.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- *... and 2 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (6 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 45 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*