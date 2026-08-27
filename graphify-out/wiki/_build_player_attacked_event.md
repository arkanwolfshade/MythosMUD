# ._build_player_attacked_event

> 32 nodes

## Key Concepts

- **test_player_effect_repository.py** (18 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **PlayerEffect** (13 connections) — `server/models/player_effect.py`
- **player_effect.py** (10 connections) — `server/models/player_effect.py`
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
- **Base** (1 connections)
- **Player effect model for the effects system (ADR-009). Persistent, tick-based…** (1 connections) — `server/models/player_effect.py`
- **Persistent player effect (status effect) with tick-based duration. Table:…** (1 connections) — `server/models/player_effect.py`
- **Unit tests for PlayerEffectRepository (ADR-009 effects system). Tests…** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_active_effects_for_player returns only effects with remaining_ticks > 0…** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **has_effect returns True when player has active effect of type.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **has_effect returns False when no active effect of type.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_effect_remaining_ticks returns duration - (current_tick - applied_at_tick).** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- *... and 7 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)

## Source Files

- `server/models/player_effect.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 61 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*