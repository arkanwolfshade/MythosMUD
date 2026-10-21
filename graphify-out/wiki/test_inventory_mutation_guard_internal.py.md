# test_inventory_mutation_guard_internal.py

> 29 nodes · cohesion 0.10

## Key Concepts

- **StatusEffect** (32 connections) — `server/models/game.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **._status_effects_list()** (5 connections) — `server/models/game.py`
- **.add_status_effect()** (4 connections) — `server/models/game.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **.remove_status_effect()** (4 connections) — `server/models/game.py`
- **test_status_effect_creation()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_duration_validation_min()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_max()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_min()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_at_duration()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_before_duration()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_permanent()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_with_source()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Represents a status effect applied to a character.** (1 connections) — `server/models/game.py`
- **Add a status effect to the player. Args: effect: StatusEffect to add** (1 connections) — `server/models/game.py`
- **Remove a status effect from the player. Args: effect_type: Type of effect to…** (1 connections) — `server/models/game.py`
- **Get all currently active status effects. Args: current_tick: Current game tick…** (1 connections) — `server/models/game.py`
- **Unit tests for StatusEffect model.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect can be created with required fields.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect can have optional source.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns True for permanent effects (duration=0).** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns True when current_tick < duration.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns False when current_tick >= duration.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- *... and 4 more nodes in this community*

## Relationships

- [test_pattern_matcher.py](test_pattern_matcher.py.md) (10 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (4 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (2 shared connections)
- [Communities (11 total, 0 thin omitted)](Communities_11_total,_0_thin_omitted.md) (2 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (1 shared connections)
- [InventoryService](InventoryService.md) (1 shared connections)
- [Client Test Remediation](Client_Test_Remediation.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*