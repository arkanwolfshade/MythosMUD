# Logging Testing Examples

> 55 nodes

## Key Concepts

- **TestRoomDataFixer** (20 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **RoomDataFixer** (14 connections) — `server/services/room_data_fixer.py`
- **.apply_room_data_fixes()** (13 connections) — `server/services/room_data_fixer.py`
- **room_data_fixer.py** (7 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_name()** (7 connections) — `server/services/room_data_fixer.py`
- **.fix_occupant_count_mismatch()** (7 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_description()** (6 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_timestamp()** (6 connections) — `server/services/room_data_fixer.py`
- **Any** (5 connections)
- **.count_applied_fixes()** (5 connections) — `server/services/room_data_fixer.py`
- **.test_apply_room_data_fixes_exception_handling()** (5 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **test_room_data_fixer.py** (4 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_name()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_name_no_error()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_name_unknown_id()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_description()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_description_no_error()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_occupant_count_mismatch()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_occupant_count_mismatch_no_error()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_occupant_count_mismatch_no_occupants()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_timestamp()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_fix_missing_timestamp_existing()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_count_applied_fixes()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_count_applied_fixes_no_fixable()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.test_apply_room_data_fixes_all_fixes()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- *... and 30 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [Room Data Fixer](Room_Data_Fixer.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/services/room_data_fixer.py`
- `server/tests/unit/services/test_room_data_fixer.py`

## Audit Trail

- EXTRACTED: 168 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*