# npc database infrastructure

> 66 nodes

## Key Concepts

- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (12 connections) — `server/services/combat_service_npc.py`
- **UUID** (11 connections)
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (11 connections) — `server/services/combat_service_npc.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc_via_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (10 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_string_id_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (8 connections) — `server/services/combat_service_npc.py`
- **.get_uuid_for_string_id()** (7 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_uuid_lookup()** (7 connections) — `server/services/combat_service_npc.py`
- **.get_original_string_id()** (6 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- **_participant_matches_npc_id()** (6 connections) — `server/services/combat_service_npc.py`
- **NPCInstanceWithRoomProtocol** (5 connections) — `server/services/combat_service_npc.py`
- **.get_player_room_id()** (4 connections) — `server/services/combat_service_npc.py`
- *... and 41 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (17 shared connections)
- [command factories exploration](command_factories_exploration.md) (10 shared connections)
- [spell game magic](spell_game_magic.md) (8 shared connections)
- [Item Instances](Item_Instances.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [combat commands handler](combat_commands_handler.md) (4 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (3 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (2 shared connections)

## Source Files

- `server/services/combat_service_npc.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 310 (96%)
- INFERRED: 13 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*