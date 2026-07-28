# Server Services (9)

> 126 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **UUID** (20 connections)
- **get_combat_id_for_npc()** (13 connections) — `server/services/combat_service_npc.py`
- **UUID** (11 connections)
- **get_npc_participant_current_room()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (10 connections) — `server/game/magic/spell_effects_internal.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (10 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (9 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc_via_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.get_uuid_for_string_id()** (7 connections) — `server/services/combat_service_npc.py`
- **combat_room_id_for_npc_spell()** (6 connections) — `server/game/magic/spell_effects_internal.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.get_original_string_id()** (6 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (6 connections) — `server/services/combat_service_npc.py`
- *... and 101 more nodes in this community*

## Relationships

- [Server Services (29)](Server_Services_%2829%29.md) (27 shared connections)
- [Server Game (7)](Server_Game_%287%29.md) (23 shared connections)
- [Server Services (28)](Server_Services_%2828%29.md) (20 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (14 shared connections)
- [Server Models (2)](Server_Models_%282%29.md) (12 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (10 shared connections)
- [Server Services (36)](Server_Services_%2836%29.md) (8 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (7 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (6 shared connections)
- [Server Services (68)](Server_Services_%2868%29.md) (6 shared connections)
- [Server App](Server_App.md) (5 shared connections)
- [Server Commands (20)](Server_Commands_%2820%29.md) (5 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`

## Audit Trail

- EXTRACTED: 550 (90%)
- INFERRED: 64 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*