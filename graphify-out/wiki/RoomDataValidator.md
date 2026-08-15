# RoomDataValidator

> 53 nodes

## Key Concepts

- **RoomDataValidator** (30 connections) — `server/services/room_data_validator.py`
- **test_room_data_validator.py** (16 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **NPCCombatIntegrationValidationMixin** (11 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.validate_room_data()** (10 connections) — `server/services/room_data_validator.py`
- **Any** (8 connections)
- **.validate_room_consistency()** (7 connections) — `server/services/room_data_validator.py`
- **.check_duplicate_occupants()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_field_types()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_required_fields()** (6 connections) — `server/services/room_data_validator.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.check_empty_room_with_occupants()** (5 connections) — `server/services/room_data_validator.py`
- **.check_occupant_count_consistency()** (5 connections) — `server/services/room_data_validator.py`
- **.is_valid_room_id()** (5 connections) — `server/services/room_data_validator.py`
- **.validate_occupant_consistency()** (4 connections) — `server/services/room_data_validator.py`
- **test_check_duplicate_occupants()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_check_duplicate_occupants_no_duplicates()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_check_empty_room_with_occupants()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_check_occupant_count_consistency()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_is_valid_room_id()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_field_types()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_field_types_valid()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_required_fields()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_required_fields_all_present()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_consistency()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **test_validate_room_data_invalid()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- *... and 28 more nodes in this community*

## Relationships

- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_room_data_validator.py`

## Audit Trail

- EXTRACTED: 93 (85%)
- INFERRED: 16 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*