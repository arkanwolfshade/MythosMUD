# Async Persistence Core

> 49 nodes

## Key Concepts

- **RoomDataValidator** (18 connections) — `server/services/room_data_validator.py`
- **test_room_data_validator.py** (16 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **.validate_room_data()** (10 connections) — `server/services/room_data_validator.py`
- **Any** (8 connections)
- **.validate_room_consistency()** (7 connections) — `server/services/room_data_validator.py`
- **.validate_required_fields()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_field_types()** (6 connections) — `server/services/room_data_validator.py`
- **.check_duplicate_occupants()** (6 connections) — `server/services/room_data_validator.py`
- **.is_valid_room_id()** (5 connections) — `server/services/room_data_validator.py`
- **.check_occupant_count_consistency()** (5 connections) — `server/services/room_data_validator.py`
- **.check_empty_room_with_occupants()** (5 connections) — `server/services/room_data_validator.py`
- **.validate_occupant_consistency()** (4 connections) — `server/services/room_data_validator.py`
- **test_validate_required_fields()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_required_fields_all_present()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_field_types()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_field_types_valid()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_data_valid()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_data_invalid()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_data_room_id()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_is_valid_room_id()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_check_occupant_count_consistency()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_check_duplicate_occupants()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_check_duplicate_occupants_no_duplicates()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_check_empty_room_with_occupants()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_consistency()** (3 connections) — `server/tests/unit/services/test_room_data_validator.py`
- *... and 24 more nodes in this community*

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [Pre-commit Hook Analysis](Pre-commit_Hook_Analysis.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Room Data Fixer](Room_Data_Fixer.md) (1 shared connections)

## Source Files

- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_room_data_validator.py`

## Audit Trail

- EXTRACTED: 156 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*