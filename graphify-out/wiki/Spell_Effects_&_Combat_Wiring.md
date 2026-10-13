# Spell Effects & Combat Wiring

> 237 nodes

## Key Concepts

- **CombatService** (202 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (32 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **test_idle_movement_combat_gate.py** (28 connections) — `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- **UUID** (23 connections)
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **test_combat_skill_wiring.py** (14 connections) — `server/tests/unit/container/test_combat_skill_wiring.py`
- **resolve_npc_participant_id_in_combat()** (13 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **_start_fight()** (10 connections) — `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- **UUID** (10 connections)
- **_attach_combat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (8 connections) — `server/services/combat_service_npc.py`
- **test_spell_effects_internal.py** (8 connections) — `server/tests/unit/game/magic/test_spell_effects_internal.py`
- **test_combat_service_npc_in_combat.py** (8 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **DataProviderProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (7 connections) — `server/services/combat_service_npc.py`
- *... and 212 more nodes in this community*

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (49 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (32 shared connections)
- [Combat Participants](Combat_Participants.md) (21 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (15 shared connections)
- [Magic & Tick Services](Magic_&_Tick_Services.md) (14 shared connections)
- [Community 126](Community_126.md) (10 shared connections)
- [Community 134](Community_134.md) (7 shared connections)
- [Community 227](Community_227.md) (6 shared connections)
- [Community 130](Community_130.md) (5 shared connections)
- [Community 427](Community_427.md) (5 shared connections)
- [Community 88](Community_88.md) (4 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (4 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/container/test_combat_skill_wiring.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 501 (83%)
- INFERRED: 102 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*