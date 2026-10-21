# TabbedInterfaceOverlay.tsx

> 19 nodes · cohesion 0.14

## Key Concepts

- **test_room_map_coordinates.py** (7 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **_as_float()** (6 connections) — `server/models/room.py`
- **.__init__()** (6 connections) — `server/models/room.py`
- **_room()** (6 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **TestRoomCoordinates** (5 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **TestAsFloat** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_booleans_are_not_coordinates()** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_coerces_every_shape_the_column_arrives_in()** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_a_room_at_the_origin_is_not_treated_as_missing()** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_to_dict_always_has_the_keys()** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_coordinates_survive_into_to_dict()** (2 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_partial_coordinates_do_not_invent_the_other_axis()** (2 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **Coerce a `numeric(10,2)` column to float. The driver hands back `Decimal` for…** (1 connections) — `server/models/room.py`
- **Initialize a Room from JSON data. Args: room_data: Dictionary containing room…** (1 connections) — `server/models/room.py`
- **parametrize** (1 connections)
- **`Room` carries map coordinates end to end (#829). `GET /api/rooms/list`…** (1 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **bool is a subclass of int, so a naive isinstance check would make True == 1.0.** (1 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **The client distinguishes "no coordinates" from "not sent"; the keys must exist…** (1 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **(0, 0) is a real cell. Truthiness checks on coordinates are a classic bug.** (1 connections) — `server/tests/unit/models/test_room_map_coordinates.py`

## Relationships

- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_map_coordinates.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*