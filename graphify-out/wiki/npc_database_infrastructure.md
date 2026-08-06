# npc database infrastructure

> 133 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **UUID** (20 connections)
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
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.get_original_string_id()** (6 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- *... and 108 more nodes in this community*

## Relationships

- [subject admin controller](subject_admin_controller.md) (33 shared connections)
- [command factories exploration](command_factories_exploration.md) (25 shared connections)
- [spell game magic](spell_game_magic.md) (21 shared connections)
- [Item Instances](Item_Instances.md) (17 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (10 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [EdgeCreationModal map STANDARD](EdgeCreationModal_map_STANDARD.md) (8 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (7 shared connections)
- [player look commands](player_look_commands.md) (7 shared connections)
- [room renderer functions](room_renderer_functions.md) (6 shared connections)
- [combat flee commands](combat_flee_commands.md) (5 shared connections)
- [player event realtime](player_event_realtime.md) (5 shared connections)

## Source Files

- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 607 (92%)
- INFERRED: 55 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*