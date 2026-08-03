# room validator services

> 81 nodes

## Key Concepts

- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **RoomDataValidator** (18 connections) — `server/services/room_data_validator.py`
- **test_room_data_validator.py** (16 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.validate_room_data()** (10 connections) — `server/services/room_data_validator.py`
- **Any** (8 connections)
- **room_data_validator.py** (7 connections) — `server/services/room_data_validator.py`
- **.validate_room_consistency()** (7 connections) — `server/services/room_data_validator.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (6 connections)
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.validate_required_fields()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_field_types()** (6 connections) — `server/services/room_data_validator.py`
- **.check_duplicate_occupants()** (6 connections) — `server/services/room_data_validator.py`
- **._validate_and_get_npc_instance()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.is_valid_room_id()** (5 connections) — `server/services/room_data_validator.py`
- **.check_occupant_count_consistency()** (5 connections) — `server/services/room_data_validator.py`
- **.check_empty_room_with_occupants()** (5 connections) — `server/services/room_data_validator.py`
- **.get_combat_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.validate_occupant_consistency()** (4 connections) — `server/services/room_data_validator.py`
- *... and 56 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (21 shared connections)
- [room fixer services](room_fixer_services.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [command input commands](command_input_commands.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_room_data_validator.py`

## Audit Trail

- EXTRACTED: 263 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*