# RoomDataValidator

> 27 nodes

## Key Concepts

- **RoomDataValidator** (30 connections) — `server/services/room_data_validator.py`
- **test_room_data_validator.py** (16 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **.validate_room_data()** (10 connections) — `server/services/room_data_validator.py`
- **Any** (8 connections)
- **.validate_field_types()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_required_fields()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_occupant_consistency()** (4 connections) — `server/services/room_data_validator.py`
- **test_validate_field_types()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_field_types_valid()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_required_fields()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_required_fields_all_present()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_data_invalid()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_data_room_id()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_data_valid()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Validate occupant count consistency. Args: room_data: Room data to validate…** (1 connections) — `server/services/room_data_validator.py`
- **Validates room data structure and content.** (1 connections) — `server/services/room_data_validator.py`
- **Validate room data structure and content. Args: room_data: Room data to…** (1 connections) — `server/services/room_data_validator.py`
- **Validate that all required fields are present. Args: room_data: Room data to…** (1 connections) — `server/services/room_data_validator.py`
- **Validate field types. Args: room_data: Room data to validate Returns:…** (1 connections) — `server/services/room_data_validator.py`
- **Unit tests for room_data_validator. Tests the RoomDataValidator class methods.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Test validate_required_fields() detects missing fields.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Test validate_required_fields() passes when all fields present.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Test validate_field_types() detects type mismatches.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Test validate_field_types() passes with correct types.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Test validate_room_data() returns is_valid=True for valid data.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`
- *... and 2 more nodes in this community*

## Relationships

- [.validate_room_consistency](validate_room_consistency.md) (8 shared connections)
- [.check_duplicate_occupants](check_duplicate_occupants.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [.get_data_provider](get_data_provider.md) (4 shared connections)
- [.check_empty_room_with_occupants](check_empty_room_with_occupants.md) (4 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (3 shared connections)

## Source Files

- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_room_data_validator.py`

## Audit Trail

- EXTRACTED: 60 (80%)
- INFERRED: 15 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*