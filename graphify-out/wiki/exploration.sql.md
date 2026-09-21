# exploration.sql

> 10 nodes

## Key Concepts

- **exploration.sql** (8 connections) — `db/procedures/exploration.sql`
- **player_exploration** (5 connections) — `db/schema.sql`
- **schema_name.get_room_id_by_stable_id()** (2 connections) — `db/procedures/exploration.sql`
- **schema_name.is_room_explored()** (2 connections) — `db/procedures/exploration.sql`
- **is_room_explored()** (2 connections) — `db/schema.sql`
- **schema_name.get_coordinate_conflicts()** (1 connections) — `db/procedures/exploration.sql`
- **schema_name.get_explored_rooms()** (1 connections) — `db/procedures/exploration.sql`
- **schema_name.get_room_exits_for_coordinate_generation()** (1 connections) — `db/procedures/exploration.sql`
- **schema_name.get_rooms_for_coordinate_generation()** (1 connections) — `db/procedures/exploration.sql`
- **schema_name.mark_room_explored()** (1 connections) — `db/procedures/exploration.sql`

## Relationships

- [rooms](rooms.md) (3 shared connections)
- [schema.sql](schema.sql.md) (2 shared connections)
- [players](players.md) (1 shared connections)

## Source Files

- `db/procedures/exploration.sql`
- `db/schema.sql`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*