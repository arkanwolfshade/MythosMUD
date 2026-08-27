# utils/config.ts

> 17 nodes

## Key Concepts

- **asyncio** (20 connections)
- **test_process_tick_regeneration_fractional_accumulation()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_sitting_position()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_respects_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_uses_magic_service()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_at_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_player_not_found()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() accumulates fractional MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() returns error when player not found.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() returns message when MP already at max.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() respects max_mp limit.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() uses magic_service if available.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() uses REST multiplier for sitting position.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [test_validate_codacy_coverage_gate.py](test_validate_codacy_coverage_gate.py.md) (8 shared connections)
- [test_process_room_rows_zone_without_slash](test_process_room_rows_zone_without_slash.md) (1 shared connections)
- [unit/middleware/__init__.py](unit-middleware-__init__.py.md) (1 shared connections)
- [test_build_room_objects_without_environment_in_attributes](test_build_room_objects_without_environment_in_attributes.md) (1 shared connections)
- [test_process_room_rows_with_none_attributes](test_process_room_rows_with_none_attributes.md) (1 shared connections)
- [test_build_room_objects_with_dict_attributes](test_build_room_objects_with_dict_attributes.md) (1 shared connections)
- [server/tests/conftest.py](server-tests-conftest.py.md) (1 shared connections)
- [test_process_room_rows_with_partial_room_id](test_process_room_rows_with_partial_room_id.md) (1 shared connections)
- [test_process_exit_rows_zone_single_part](test_process_exit_rows_zone_single_part.md) (1 shared connections)
- [test_process_room_rows_empty_list](test_process_room_rows_empty_list.md) (1 shared connections)
- [test_create_lie_command](test_create_lie_command.md) (1 shared connections)
- [test_load_room_cache_with_rooms_logs_sample_ids](test_load_room_cache_with_rooms_logs_sample_ids.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*