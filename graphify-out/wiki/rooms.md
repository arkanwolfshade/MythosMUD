# rooms

> 27 nodes

## Key Concepts

- **rooms** (15 connections) — `db/schema.sql`
- **rooms.sql** (13 connections) — `db/procedures/rooms.sql`
- **zones** (5 connections) — `db/schema.sql`
- **schema_name.count_coordinated_rooms()** (4 connections) — `db/procedures/exploration.sql`
- **count_coordinated_rooms()** (4 connections) — `db/schema.sql`
- **subzones** (4 connections)
- **schema_name.create_room_link()** (2 connections) — `db/procedures/rooms.sql`
- **schema_name.delete_room_link()** (2 connections) — `db/procedures/rooms.sql`
- **schema_name.update_room_link()** (2 connections) — `db/procedures/rooms.sql`
- **create_room_link()** (2 connections) — `db/schema.sql`
- **delete_room_link()** (2 connections) — `db/schema.sql`
- **get_room_id_by_stable_id()** (2 connections) — `db/schema.sql`
- **room_links** (2 connections) — `db/schema.sql`
- **update_npc_definition()** (2 connections) — `db/schema.sql`
- **update_room_link()** (2 connections) — `db/schema.sql`
- **zone_configurations** (2 connections)
- **subzones** (1 connections)
- **schema_name.clear_room_map_origins()** (1 connections) — `db/procedures/rooms.sql`
- **schema_name.get_room_by_stable_id()** (1 connections) — `db/procedures/rooms.sql`
- **schema_name.get_room_exits()** (1 connections) — `db/procedures/rooms.sql`
- **schema_name.get_room_stable_ids_by_uuids()** (1 connections) — `db/procedures/rooms.sql`
- **schema_name.get_rooms_by_zone_pattern()** (1 connections) — `db/procedures/rooms.sql`
- **schema_name.get_rooms_with_exits()** (1 connections) — `db/procedures/rooms.sql`
- **schema_name.set_room_map_origin()** (1 connections) — `db/procedures/rooms.sql`
- **schema_name.update_room_map_position()** (1 connections) — `db/procedures/rooms.sql`
- *... and 2 more nodes in this community*

## Relationships

- [schema.sql](schema.sql.md) (9 shared connections)
- [exploration.sql](exploration.sql.md) (3 shared connections)

## Source Files

- `db/procedures/exploration.sql`
- `db/procedures/rooms.sql`
- `db/schema.sql`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*