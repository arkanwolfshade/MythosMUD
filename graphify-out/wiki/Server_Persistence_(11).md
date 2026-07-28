# Server Persistence (11)

> 30 nodes

## Key Concepts

- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **test_player_effect_repository.py** (17 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **player_effect.py** (9 connections) — `server/models/player_effect.py`
- **_make_effect()** (6 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_row_from_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_active_effects_for_player_filters_by_remaining()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_true()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_add_effect_returns_id()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_delete_effect()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_false()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks_none()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_expire_effects_for_tick_returns_expired_and_deletes()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Base** (1 connections)
- **Player effect model for the effects system (ADR-009).  Persistent, tick-based st** (1 connections) — `server/models/player_effect.py`
- **Persistent player effect (status effect) with tick-based duration.      Table: p** (1 connections) — `server/models/player_effect.py`
- **player_id()** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Unit tests for PlayerEffectRepository (ADR-009 effects system).  Tests add_effec** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Create PlayerEffectRepository instance.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Build a mock PlayerEffect with given fields.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Build a procedure result row (mappings().all() item) from effect mock.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **add_effect persists effect and returns effect id (via add_player_effect procedur** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **delete_effect removes effect by id.** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **get_active_effects_for_player returns only effects with remaining_ticks > 0 (pro** (1 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- *... and 5 more nodes in this community*

## Relationships

- [Server Persistence (8)](Server_Persistence_%288%29.md) (9 shared connections)
- [Server Services](Server_Services.md) (5 shared connections)
- [Server Models (17)](Server_Models_%2817%29.md) (3 shared connections)
- [Server Models (14)](Server_Models_%2814%29.md) (2 shared connections)
- [Server Services (52)](Server_Services_%2852%29.md) (1 shared connections)
- [Server Models (21)](Server_Models_%2821%29.md) (1 shared connections)

## Source Files

- `server/models/player_effect.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 86 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*