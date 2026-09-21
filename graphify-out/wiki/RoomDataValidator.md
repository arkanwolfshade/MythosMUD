# RoomDataValidator

> 79 nodes

## Key Concepts

- **RoomDataValidator** (30 connections) — `server/services/room_data_validator.py`
- **_NPCCombatIntegrationValidationDeps** (18 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **test_room_data_validator.py** (16 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.validate_room_data()** (10 connections) — `server/services/room_data_validator.py`
- **Any** (8 connections)
- **.validate_room_consistency()** (7 connections) — `server/services/room_data_validator.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.check_duplicate_occupants()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_field_types()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_required_fields()** (6 connections) — `server/services/room_data_validator.py`
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_and_get_npc_instance()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.check_empty_room_with_occupants()** (5 connections) — `server/services/room_data_validator.py`
- **.check_occupant_count_consistency()** (5 connections) — `server/services/room_data_validator.py`
- **.is_valid_room_id()** (5 connections) — `server/services/room_data_validator.py`
- **UUID** (5 connections)
- **.get_combat_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.validate_occupant_consistency()** (4 connections) — `server/services/room_data_validator.py`
- **test_check_duplicate_occupants()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- *... and 54 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_room_data_validator.py`

## Audit Trail

- EXTRACTED: 136 (87%)
- INFERRED: 20 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*