# Container Persistence Ops

> 295 nodes

## Key Concepts

- **ExplorationService** (73 connections) — `server/services/exploration_service.py`
- **RoomService** (72 connections) — `server/game/room_service.py`
- **maps.py** (63 connections) — `server/api/maps.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (22 connections) — `server/api/map_helpers.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **get_ascii_map()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **Any** (13 connections)
- **get_ascii_minimap()** (12 connections) — `server/api/maps.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **.get_room()** (11 connections) — `server/game/room_service.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- *... and 270 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (29 shared connections)
- [Client Event Store](Client_Event_Store.md) (18 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (18 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (14 shared connections)
- [Map Room Helpers](Map_Room_Helpers.md) (12 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (10 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (9 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (8 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (7 shared connections)
- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (5 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (5 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (4 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/ascii_map_renderer.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 1268 (94%)
- INFERRED: 80 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*