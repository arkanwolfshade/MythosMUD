# server tests unit game magic

> 17 nodes

## Key Concepts

- **asyncio** (20 connections)
- **test_process_tick_regeneration_calculates_max_from_power()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_sitting_position()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_respects_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_uses_magic_service()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_at_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_player_not_found()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() returns error when player not found.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() returns message when MP already at max.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() respects max_mp limit.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() uses magic_service if available.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() uses REST multiplier for sitting position.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() calculates max_mp from power if not present.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [server tests unit game magic](server_tests_unit_game_magic.md) (20 shared connections)

## Source Files

- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*