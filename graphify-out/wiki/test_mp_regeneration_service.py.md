# test_mp_regeneration_service.py

> 16 nodes

## Key Concepts

- **test_mp_regeneration_service.py** (34 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_player_not_found()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_higher_than_rest()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_default_position()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_lying()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_sitting()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_standing()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Unit tests for MP regeneration service. Tests the MPRegenerationService class…** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test _get_regen_multiplier() returns 1.0 for standing position.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test _get_regen_multiplier() returns REST multiplier for sitting.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test _get_regen_multiplier() returns enhanced REST multiplier for lying.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test _get_regen_multiplier() defaults to 1.0 when position not specified.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() restores more MP than rest.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() returns error when player not found.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [asyncio](asyncio.md) (12 shared connections)
- [mp_regeneration_service](mp_regeneration_service.md) (4 shared connections)
- [MPRegenerationService](MPRegenerationService.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_process_tick_regeneration_fractional_accumulation](test_process_tick_regeneration_fractional_accumulation.md) (1 shared connections)
- [test_restore_mp_from_rest_at_max](test_restore_mp_from_rest_at_max.md) (1 shared connections)
- [test_restore_mp_from_rest_calculates_max_from_power](test_restore_mp_from_rest_calculates_max_from_power.md) (1 shared connections)
- [test_restore_mp_from_meditation_player_not_found](test_restore_mp_from_meditation_player_not_found.md) (1 shared connections)
- [test_process_tick_regeneration_sitting_position](test_process_tick_regeneration_sitting_position.md) (1 shared connections)
- [test_process_tick_regeneration_player_not_found](test_process_tick_regeneration_player_not_found.md) (1 shared connections)
- [test_process_tick_regeneration_at_max](test_process_tick_regeneration_at_max.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*