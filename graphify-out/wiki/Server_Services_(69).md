# Server Services (69)

> 23 nodes

## Key Concepts

- **RoomDataFixer** (14 connections) — `server/services/room_data_fixer.py`
- **.apply_room_data_fixes()** (13 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_name()** (7 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_description()** (6 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_timestamp()** (6 connections) — `server/services/room_data_fixer.py`
- **Any** (5 connections)
- **.count_applied_fixes()** (5 connections) — `server/services/room_data_fixer.py`
- **.test_apply_room_data_fixes_exception_handling()** (5 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_name_no_error()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_count_applied_fixes()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_apply_room_data_fixes_all_fixes()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_apply_room_data_fixes_preserves_original()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **Applies automatic fixes to room data when validation issues are detected.** (1 connections) — `server/services/room_data_fixer.py`
- **Fix missing name field.** (1 connections) — `server/services/room_data_fixer.py`
- **Fix missing description field.** (1 connections) — `server/services/room_data_fixer.py`
- **Fix missing timestamp field.** (1 connections) — `server/services/room_data_fixer.py`
- **Count the number of fixes that were applied.** (1 connections) — `server/services/room_data_fixer.py`
- **Apply automatic fixes to room data when possible.          Args:             roo** (1 connections) — `server/services/room_data_fixer.py`
- **Test fix_missing_name does nothing when no error.** (1 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **Test count_applied_fixes counts fixable errors.** (1 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **Test apply_room_data_fixes applies all fixes.** (1 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **Test apply_room_data_fixes does not modify original data.** (1 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **Test apply_room_data_fixes handles exceptions.** (1 connections) — `server/tests/unit/services/test_room_data_fixer.py`

## Relationships

- [Server Services (55)](Server_Services_%2855%29.md) (19 shared connections)
- [Server Services (20)](Server_Services_%2820%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server Events](Server_Events.md) (1 shared connections)
- [Server Services (35)](Server_Services_%2835%29.md) (1 shared connections)

## Source Files

- `server/services/room_data_fixer.py`
- `server/tests/unit/services/test_room_data_fixer.py`

## Audit Trail

- EXTRACTED: 79 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*