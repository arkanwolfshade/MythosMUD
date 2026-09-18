# Community 893

> 17 nodes

## Key Concepts

- **test_room_map_coordinates.py** (7 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **_as_float()** (6 connections) — `server/models/room.py`
- **_room()** (6 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **TestRoomCoordinates** (5 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **TestAsFloat** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_booleans_are_not_coordinates()** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_coerces_every_shape_the_column_arrives_in()** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_a_room_at_the_origin_is_not_treated_as_missing()** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_to_dict_always_has_the_keys()** (3 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_coordinates_survive_into_to_dict()** (2 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.test_partial_coordinates_do_not_invent_the_other_axis()** (2 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **parametrize** (1 connections)
- **Coerce a `numeric(10,2)` column to float. The driver hands back `Decimal` for…** (1 connections) — `server/models/room.py`
- **`Room` carries map coordinates end to end (#829). `GET /api/rooms/list`…** (1 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **bool is a subclass of int, so a naive isinstance check would make True == 1.0.** (1 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **The client distinguishes "no coordinates" from "not sent"; the keys must exist…** (1 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **(0, 0) is a real cell. Truthiness checks on coordinates are a classic bug.** (1 connections) — `server/tests/unit/models/test_room_map_coordinates.py`

## Relationships

- [Community 95](Community_95.md) (3 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_map_coordinates.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*