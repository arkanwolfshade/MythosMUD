# .get_data_provider

> 12 nodes

## Key Concepts

- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_and_get_npc_instance()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.is_valid_room_id()** (5 connections) — `server/services/room_data_validator.py`
- **test_is_valid_room_id()** (4 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **_warn_attacked_dead_npc()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Validate that player and NPC are in the same room.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Log when a player targets an NPC that exists but is not alive.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return data provider dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Validate NPC instance (lookup when missing). Return instance or None.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Validate room ID format. Args: room_id: Room ID to validate Returns: bool: True…** (1 connections) — `server/services/room_data_validator.py`
- **Test is_valid_room_id() validates room ID format.** (1 connections) — `server/tests/unit/services/test_room_data_validator.py`

## Relationships

- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (4 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_room_data_validator.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*