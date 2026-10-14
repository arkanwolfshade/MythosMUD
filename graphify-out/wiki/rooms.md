# rooms

> 38 nodes

## Key Concepts

- **rooms** (16 connections) — `db/schema.sql`
- **rooms.sql** (13 connections) — `db/procedures/rooms.sql`
- **exploration.sql** (8 connections) — `db/procedures/exploration.sql`
- **zones** (6 connections) — `db/schema.sql`
- **player_exploration** (5 connections) — `db/schema.sql`
- **schema_name.count_coordinated_rooms()** (4 connections) — `db/procedures/exploration.sql`
- **schema_name.update_room_properties()** (4 connections) — `db/procedures/rooms.sql`
- **count_coordinated_rooms()** (4 connections) — `db/schema.sql`
- **subzones** (4 connections)
- **schema_name.get_room_id_by_stable_id()** (2 connections) — `db/procedures/exploration.sql`
- **schema_name.is_room_explored()** (2 connections) — `db/procedures/exploration.sql`
- **schema_name.create_room_link()** (2 connections) — `db/procedures/rooms.sql`
- **schema_name.delete_room_link()** (2 connections) — `db/procedures/rooms.sql`
- **schema_name.update_room_link()** (2 connections) — `db/procedures/rooms.sql`
- **create_room_link()** (2 connections) — `db/schema.sql`
- **delete_room_link()** (2 connections) — `db/schema.sql`
- **get_room_id_by_stable_id()** (2 connections) — `db/schema.sql`
- **is_room_explored()** (2 connections) — `db/schema.sql`
- **room_links** (2 connections) — `db/schema.sql`
- **update_npc_definition()** (2 connections) — `db/schema.sql`
- **update_room_link()** (2 connections) — `db/schema.sql`
- **zone_configurations** (2 connections)
- **schema_name.get_coordinate_conflicts()** (1 connections) — `db/procedures/exploration.sql`
- **schema_name.get_explored_rooms()** (1 connections) — `db/procedures/exploration.sql`
- **schema_name.get_room_exits_for_coordinate_generation()** (1 connections) — `db/procedures/exploration.sql`
- *... and 13 more nodes in this community*

## Relationships

- [schema.sql](schema.sql.md) (11 shared connections)
- [players](players.md) (1 shared connections)

## Source Files

- `db/procedures/exploration.sql`
- `db/procedures/rooms.sql`
- `db/schema.sql`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*