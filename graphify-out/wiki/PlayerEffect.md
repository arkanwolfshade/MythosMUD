# PlayerEffect

> 30 nodes · cohesion 0.09

## Key Concepts

- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **test_player_effect_repository.py** (17 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **player_effect.py** (9 connections) — `server/models/player_effect.py`
- **_make_effect()** (6 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
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
- **Base** (1 connections)
- **Player effect model for the effects system (ADR-009).  Persistent, tick-based st** (1 connections) — `server/models/player_effect.py`
- **Persistent player effect (status effect) with tick-based duration.      Table: p** (1 connections) — `server/models/player_effect.py`
- **player_id()** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Unit tests for PlayerEffectRepository (ADR-009 effects system).  Tests add_effec** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_active_effects_for_player returns only effects with remaining_ticks > 0 (pro** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **has_effect returns True when player has active effect of type.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **has_effect returns False when no active effect of type.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_effect_remaining_ticks returns duration - (current_tick - applied_at_tick).** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_effect_remaining_ticks returns None when no matching effect.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **expire_effects_for_tick returns (player_id, effect_type) and deletes rows via pr** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- *... and 5 more nodes in this community*

## Relationships

- [player_effect_repository.py](player_effect_repository.py.md) (9 shared connections)
- [Player](Player.md) (4 shared connections)
- [Base](Base.md) (3 shared connections)
- [__init__.py](__init__.py.md) (2 shared connections)
- [PlayerInventory](PlayerInventory.md) (2 shared connections)
- [PlayerChannelPreferences](PlayerChannelPreferences.md) (1 shared connections)

## Source Files

- `server/models/player_effect.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 86 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*