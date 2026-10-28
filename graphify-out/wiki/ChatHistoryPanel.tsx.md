# ChatHistoryPanel.tsx

> 113 nodes · cohesion 0.03

## Key Concepts

- **NPCOccupantProcessor** (32 connections) — `server/realtime/npc_occupant_processor.py`
- **RoomIDUtils** (30 connections) — `server/realtime/room_id_utils.py`
- **RoomOccupantManager** (25 connections) — `server/realtime/room_occupant_manager.py`
- **room_occupant_manager.py** (22 connections) — `server/realtime/room_occupant_manager.py`
- **test_npc_occupant_processor.py** (20 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Any** (11 connections)
- **npc_occupant_processor.py** (10 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **room_id_utils.py** (6 connections) — `server/realtime/room_id_utils.py`
- **.get_room_occupants()** (6 connections) — `server/realtime/room_occupant_manager.py`
- **._filter_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_lifecycle_manager_for_filtering()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._scan_active_npcs_for_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._should_include_npc_in_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._validate_npc_room_tracking()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **.check_normalized_ids_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_room_matches()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_npc_room_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **._filter_single_fallback_npc()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- *... and 88 more nodes in this community*

## Relationships

- [Room](Room.md) (8 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (8 shared connections)
- [session](session.md) (5 shared connections)
- [look_container.py](look_container.py.md) (5 shared connections)
- [test_lint_pyright_suppressions.py](test_lint_pyright_suppressions.py.md) (5 shared connections)
- [Communities (355 total, 223 thin omitted)](Communities_355_total,_223_thin_omitted.md) (4 shared connections)
- [ResourceManager](ResourceManager.md) (4 shared connections)
- [command_parser.py](command_parser.py.md) (3 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [PlayerRespawnWrapper](PlayerRespawnWrapper.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 199 (84%)
- INFERRED: 37 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*