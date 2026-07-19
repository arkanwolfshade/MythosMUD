# Combat NPC Lookup

> 52 nodes · cohesion 0.08

## Key Concepts

- **combat_service_npc.py** (25 connections) — `server/services/combat_service_npc.py`
- **CombatService** (14 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc()** (13 connections) — `server/services/combat_service_npc.py`
- **UUID** (12 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (10 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (10 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (9 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc_via_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **_get_uuid_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (6 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_string_id_mapping()** (6 connections) — `server/services/combat_service_npc.py`
- **_participant_matches_npc_id()** (6 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (6 connections) — `server/services/combat_service_npc.py`
- **.get_uuid_for_string_id()** (6 connections) — `server/services/combat_service_npc.py`
- **CombatInstance** (5 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_uuid_lookup()** (5 connections) — `server/services/combat_service_npc.py`
- **.get_original_string_id()** (5 connections) — `server/services/combat_service_npc.py`
- **CombatParticipant** (4 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (4 connections) — `server/services/combat_service_npc.py`
- *... and 27 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (16 shared connections)
- [[Spell Effect Protocols]] (6 shared connections)
- [[Combat Taunt Tests]] (3 shared connections)
- [[Player Combat XP]] (3 shared connections)
- [[Combat Command Handler]] (2 shared connections)

## Source Files

- `server/services/combat_service_npc.py`

## Audit Trail

- EXTRACTED: 233 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
