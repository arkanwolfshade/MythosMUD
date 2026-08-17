# asyncio

> 23 nodes

## Key Concepts

- **asyncio** (20 connections)
- **test_process_tick_regeneration_at_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_calculates_max_from_power()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_lying_position()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_sitting_position()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_respects_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_at_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_player_not_found()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_rest_at_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_rest_calculates_max_from_power()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_rest_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() returns message when MP already at max.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() calculates max_mp from power if not present.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() returns error when player not found.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() returns message when MP already at max.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() respects max_mp limit.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() uses REST multiplier for sitting position.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() uses enhanced REST multiplier for lying…** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() returns zero when MP already at max.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() calculates max_mp from power if not present.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (13 shared connections)
- [test_process_tick_regeneration_fractional_accumulation](test_process_tick_regeneration_fractional_accumulation.md) (1 shared connections)
- [test_process_tick_regeneration_player_not_found](test_process_tick_regeneration_player_not_found.md) (1 shared connections)
- [test_process_tick_regeneration_restores_mp](test_process_tick_regeneration_restores_mp.md) (1 shared connections)
- [test_restore_mp_from_item_calculates_max_from_power](test_restore_mp_from_item_calculates_max_from_power.md) (1 shared connections)
- [test_restore_mp_from_item_player_not_found](test_restore_mp_from_item_player_not_found.md) (1 shared connections)
- [test_restore_mp_from_item_uses_magic_service](test_restore_mp_from_item_uses_magic_service.md) (1 shared connections)
- [test_restore_mp_from_rest_player_not_found](test_restore_mp_from_rest_player_not_found.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*