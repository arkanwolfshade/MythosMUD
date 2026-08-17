# combat_service_npc.py

> 68 nodes

## Key Concepts

- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (31 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **UUID** (10 connections)
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
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
- *... and 43 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (25 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [CombatParticipant](CombatParticipant.md) (8 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [spell_effects_internal.py](spell_effects_internal.py.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [_validate_taunt_context](_validate_taunt_context.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/combat_service_npc.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 165 (91%)
- INFERRED: 17 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*