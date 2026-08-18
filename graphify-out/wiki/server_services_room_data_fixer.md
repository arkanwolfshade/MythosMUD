# server services room data fixer

> 52 nodes

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
- *... and 27 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server realtime event handler rationale](server_realtime_event_handler_rationale.md) (2 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)

## Source Files

- `server/services/room_data_fixer.py`
- `server/tests/unit/services/test_room_data_fixer.py`

## Audit Trail

- EXTRACTED: 82 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*