# server services combat service npc

> 64 nodes

## Key Concepts

- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (31 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **UUID** (10 connections)
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (8 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_string_id_mapping()** (7 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_uuid_lookup()** (6 connections) — `server/services/combat_service_npc.py`
- **_participant_matches_npc_id()** (5 connections) — `server/services/combat_service_npc.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_service_npc.py`
- **.get_uuid_for_string_id()** (4 connections) — `server/services/combat_service_npc.py`
- **test_get_participant_current_room_player()** (4 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **test_resolve_npc_participant_id_in_combat_by_uuid()** (4 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **test_sync_npc_participant_dp_after_spell_damage()** (4 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **NPCInstanceWithRoomProtocol** (3 connections) — `server/services/combat_service_npc.py`
- *... and 39 more nodes in this community*

## Relationships

- [server events combat events](server_events_combat_events.md) (26 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (10 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (8 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (6 shared connections)
- [server models combat](server_models_combat.md) (4 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (3 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/services/combat_service_npc.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 158 (91%)
- INFERRED: 15 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*