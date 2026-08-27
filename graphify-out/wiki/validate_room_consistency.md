# .validate_room_consistency

> 8 nodes

## Key Concepts

- **.validate_room_consistency()** (7 connections) — `server/services/room_data_validator.py`
- **.check_occupant_count_consistency()** (5 connections) — `server/services/room_data_validator.py`
- **test_check_occupant_count_consistency()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_consistency()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Check if occupant count matches the actual occupants list length. Args:…** (1 connections) — `server/services/room_data_validator.py`
- **Validate room data consistency. Args: room_data: Room data to validate for…** (1 connections) — `server/services/room_data_validator.py`
- **Test validate_room_consistency() validates room consistency.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Test check_occupant_count_consistency() detects mismatches.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`

## Relationships

- [RoomDataValidator](RoomDataValidator.md) (8 shared connections)
- [.check_duplicate_occupants](check_duplicate_occupants.md) (1 shared connections)
- [.check_empty_room_with_occupants](check_empty_room_with_occupants.md) (1 shared connections)

## Source Files

- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_room_data_validator.py`

## Audit Trail

- EXTRACTED: 15 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*