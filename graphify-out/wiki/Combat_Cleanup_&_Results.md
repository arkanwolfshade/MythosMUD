# Combat Cleanup & Results

> 193 nodes

## Key Concepts

- **CombatService** (155 connections) — `server/services/combat_service.py`
- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **UUID** (20 connections)
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **NPCCombatIntegrationCombatMixin** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **broadcast_aggro_target_switches()** (8 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (8 connections) — `server/services/combat_service_events.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (8 connections)
- **test_combat_service_npc_in_combat.py** (8 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- *... and 168 more nodes in this community*

## Relationships

- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (43 shared connections)
- [Community 46](Community_46.md) (39 shared connections)
- [Combat Events](Combat_Events.md) (38 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (28 shared connections)
- [Community 152](Community_152.md) (26 shared connections)
- [Community 63](Community_63.md) (14 shared connections)
- [Community 275](Community_275.md) (13 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (11 shared connections)
- [Community 277](Community_277.md) (8 shared connections)
- [Community 273](Community_273.md) (6 shared connections)
- [Community 82](Community_82.md) (6 shared connections)
- [Community 261](Community_261.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_persistence_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 542 (87%)
- INFERRED: 83 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*