# Container Data Models

> 88 nodes

## Key Concepts

- **test_npc_utils.py** (30 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (11 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (8 connections) — `server/npc/npc_utils.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **.is_required()** (4 connections) — `server/models/npc.py`
- **.get_zone_configuration()** (4 connections) — `server/npc/population_control.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **Any** (3 connections)
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **test_extract_room_id_from_npc_current_room()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_current_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_not_found()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_non_string()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 63 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (16 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (4 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (2 shared connections)
- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (1 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (1 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 271 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*