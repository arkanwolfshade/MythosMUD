# .end combat()

> 56 nodes

## Key Concepts

- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc()** (13 connections) — `server/services/combat_service_npc.py`
- **UUID** (11 connections)
- **get_npc_participant_current_room()** (11 connections) — `server/services/combat_service_npc.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (10 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (9 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc_via_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **.get_uuid_for_string_id()** (7 connections) — `server/services/combat_service_npc.py`
- **.get_original_string_id()** (6 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (6 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (6 connections) — `server/services/combat_service_npc.py`
- **_participant_matches_npc_id()** (6 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_string_id_mapping()** (6 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (6 connections) — `server/services/combat_service_npc.py`
- **.end_combat_if_npc_died()** (5 connections) — `server/services/combat_service.py`
- **NPCInstanceWithRoomProtocol** (5 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_uuid_lookup()** (5 connections) — `server/services/combat_service_npc.py`
- **._get_combat_id_for_npc()** (4 connections) — `server/services/combat_service.py`
- *... and 31 more nodes in this community*

## Relationships

- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (27 shared connections)
- [combat](combat.md) (11 shared connections)
- [Spell Targeting](Spell_Targeting.md) (8 shared connections)
- [get current tick()](get_current_tick%28%29.md) (3 shared connections)
- [combat taunt](combat_taunt.md) (3 shared connections)

## Source Files

- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`

## Audit Trail

- EXTRACTED: 237 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*