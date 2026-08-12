# TestRoomDataFixer

> 53 nodes

## Key Concepts

- **TestRoomDataFixer** (20 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **RoomDataFixer** (13 connections) — `server/services/room_data_fixer.py`
- **.apply_room_data_fixes()** (13 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_name()** (7 connections) — `server/services/room_data_fixer.py`
- **.fix_occupant_count_mismatch()** (7 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_description()** (6 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_timestamp()** (6 connections) — `server/services/room_data_fixer.py`
- **.count_applied_fixes()** (5 connections) — `server/services/room_data_fixer.py`
- **Any** (5 connections)
- **.test_apply_room_data_fixes_exception_handling()** (4 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **test_room_data_fixer.py** (4 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_apply_room_data_fixes_all_fixes()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_apply_room_data_fixes_invalid_input()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_apply_room_data_fixes_no_errors()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_apply_room_data_fixes_preserves_original()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_count_applied_fixes()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_count_applied_fixes_no_fixable()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_description()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_description_no_error()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_name()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_name_no_error()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_name_unknown_id()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_timestamp()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_timestamp_existing()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_occupant_count_mismatch()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- *... and 28 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [Any](Any.md) (1 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/services/room_data_fixer.py`
- `server/tests/unit/services/test_room_data_fixer.py`

## Audit Trail

- EXTRACTED: 160 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*