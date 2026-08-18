# asyncio

> 19 nodes

## Key Concepts

- **asyncio** (20 connections)
- **test_process_tick_regeneration_at_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_lying_position()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_calculates_max_from_power()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_higher_than_rest()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_rest_player_not_found()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_rest_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() returns error when player not found.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() restores more MP than rest.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() calculates max_mp from power if not present.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() uses enhanced REST multiplier for lying…** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() returns zero when MP already at max.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (12 shared connections)
- [test_process_tick_regeneration_calculates_max_from_power](test_process_tick_regeneration_calculates_max_from_power.md) (1 shared connections)
- [test_process_tick_regeneration_fractional_accumulation](test_process_tick_regeneration_fractional_accumulation.md) (1 shared connections)
- [test_process_tick_regeneration_player_not_found](test_process_tick_regeneration_player_not_found.md) (1 shared connections)
- [test_process_tick_regeneration_sitting_position](test_process_tick_regeneration_sitting_position.md) (1 shared connections)
- [test_restore_mp_from_item_player_not_found](test_restore_mp_from_item_player_not_found.md) (1 shared connections)
- [test_restore_mp_from_meditation_player_not_found](test_restore_mp_from_meditation_player_not_found.md) (1 shared connections)
- [test_restore_mp_from_rest_at_max](test_restore_mp_from_rest_at_max.md) (1 shared connections)
- [test_restore_mp_from_rest_calculates_max_from_power](test_restore_mp_from_rest_calculates_max_from_power.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*