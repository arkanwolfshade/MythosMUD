# Container Persistence Ops

> 136 nodes

## Key Concepts

- **ExplorationService** (73 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (9 connections) — `server/api/maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **Any** (7 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **.mark_room_as_explored()** (7 connections) — `server/services/exploration_service.py`
- **UUID** (7 connections)
- **._get_room_uuid_by_stable_id()** (7 connections) — `server/services/exploration_service.py`
- **.is_room_explored()** (6 connections) — `server/services/exploration_service.py`
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **_CoordGenCtx** (5 connections) — `server/api/maps.py`
- **UUID** (5 connections)
- **AsyncSession** (5 connections)
- **._mark_explored_in_session()** (5 connections) — `server/services/exploration_service.py`
- **.get_explored_rooms()** (5 connections) — `server/services/exploration_service.py`
- *... and 111 more nodes in this community*

## Relationships

- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (27 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (18 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (14 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (12 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (8 shared connections)
- [Map Room Helpers](Map_Room_Helpers.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Zone Coordinate Generator](Zone_Coordinate_Generator.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 530 (93%)
- INFERRED: 37 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*