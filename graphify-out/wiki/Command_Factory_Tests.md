# Command Factory Tests

> 60 nodes

## Key Concepts

- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
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
- **.get_uuid_for_string_id()** (7 connections) — `server/services/combat_service_npc.py`
- **combat_room_id_for_npc_spell()** (6 connections) — `server/game/magic/spell_effects_internal.py`
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
- *... and 35 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (30 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (15 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (11 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`

## Audit Trail

- EXTRACTED: 255 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*