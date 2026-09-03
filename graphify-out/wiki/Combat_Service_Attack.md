# Combat Service Attack

> 184 nodes

## Key Concepts

- **CombatService** (165 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (31 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **UUID** (10 connections)
- **finalize_attack_result()** (9 connections) — `server/services/combat_service_attack.py`
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **validate_melee_location()** (8 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (8 connections) — `server/services/combat_service_attack.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **DataProviderProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- *... and 159 more nodes in this community*

## Relationships

- [Combat Events](Combat_Events.md) (43 shared connections)
- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (32 shared connections)
- [Combat Turn Processing](Combat_Turn_Processing.md) (26 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (25 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (13 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (12 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (8 shared connections)
- [Combat Taunt](Combat_Taunt.md) (6 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (6 shared connections)
- [Test Combat Service](Test_Combat_Service.md) (5 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (4 shared connections)
- [Npc Combat Integration Service](Npc_Combat_Integration_Service.md) (4 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 447 (84%)
- INFERRED: 83 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*