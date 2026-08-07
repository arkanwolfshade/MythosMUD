# models player rationale

> 130 nodes

## Key Concepts

- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatDataProvider** (39 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **test_npc_combat_data_provider.py** (17 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_processing.py`
- **npc_combat_integration_combat_mixin.py** (16 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **npc_combat_lucidity.py** (12 connections) — `server/services/npc_combat_lucidity.py`
- **NPCCombatIntegrationCombatMixin** (11 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (6 connections)
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (6 connections)
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 105 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (15 shared connections)
- [player event realtime](player_event_realtime.md) (13 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (10 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (9 shared connections)
- [grace period login](grace_period_login.md) (8 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (7 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (6 shared connections)
- [player look commands](player_look_commands.md) (5 shared connections)
- [combat commands handler](combat_commands_handler.md) (5 shared connections)
- [Item Instances](Item_Instances.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [room validator services](room_validator_services.md) (4 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 542 (94%)
- INFERRED: 37 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*