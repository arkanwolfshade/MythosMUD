# Server Services (76)

> 21 nodes

## Key Concepts

- **RoomDataValidator** (18 connections) — `server/services/room_data_validator.py`
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
- **Validates room data structure and content.** (1 connections) — `server/services/room_data_validator.py`
- **Validate room data structure and content.          Args:             room_data:** (1 connections) — `server/services/room_data_validator.py`
- **Validate that all required fields are present.          Args:             room_d** (1 connections) — `server/services/room_data_validator.py`
- **Validate field types.          Args:             room_data: Room data to validat** (1 connections) — `server/services/room_data_validator.py`
- **Validate occupant count consistency.          Args:             room_data: Room** (1 connections) — `server/services/room_data_validator.py`
- **Validate room ID format.          Args:             room_id: Room ID to validate** (1 connections) — `server/services/room_data_validator.py`
- **Check if occupant count matches the actual occupants list length.          Args:** (1 connections) — `server/services/room_data_validator.py`
- **Check for duplicate occupants in the room.          Args:             room_data:** (1 connections) — `server/services/room_data_validator.py`
- **Check if room has occupants but no name.          Args:             room_data: R** (1 connections) — `server/services/room_data_validator.py`
- **Validate room data consistency.          Args:             room_data: Room data** (1 connections) — `server/services/room_data_validator.py`

## Relationships

- [Server Services (59)](Server_Services_%2859%29.md) (14 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (4 shared connections)
- [Server Services (20)](Server_Services_%2820%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server Events](Server_Events.md) (1 shared connections)

## Source Files

- `server/services/room_data_validator.py`

## Audit Trail

- EXTRACTED: 87 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*