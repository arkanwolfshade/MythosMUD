# containers.sql

> 25 nodes

## Key Concepts

- **containers.sql** (12 connections) — `db/procedures/containers.sql`
- **item_instances** (9 connections) — `db/schema.sql`
- **container_contents** (7 connections) — `db/schema.sql`
- **schema_name.get_container_contents_json()** (4 connections) — `db/procedures/containers.sql`
- **containers** (4 connections) — `db/schema.sql`
- **get_container_contents_json()** (4 connections) — `db/schema.sql`
- **item_prototypes** (4 connections) — `db/schema.sql`
- **items.sql** (3 connections) — `db/procedures/items.sql`
- **schema_name.add_item_to_container()** (2 connections) — `db/procedures/containers.sql`
- **schema_name.item_instance_exists()** (2 connections) — `db/procedures/items.sql`
- **add_item_to_container()** (2 connections) — `db/schema.sql`
- **item_component_states** (2 connections) — `db/schema.sql`
- **item_instance_exists()** (2 connections) — `db/schema.sql`
- **schema_name.clear_container_contents()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.create_container()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.delete_container()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.fetch_container_items()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.get_container()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.get_containers_by_entity_id()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.get_containers_by_room_id()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.get_decayed_containers()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.remove_item_from_container()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.update_container()** (1 connections) — `db/procedures/containers.sql`
- **schema_name.get_item_instance()** (1 connections) — `db/procedures/items.sql`
- **schema_name.upsert_item_instance()** (1 connections) — `db/procedures/items.sql`

## Relationships

- [schema.sql](schema.sql.md) (8 shared connections)
- [players](players.md) (1 shared connections)

## Source Files

- `db/procedures/containers.sql`
- `db/procedures/items.sql`
- `db/schema.sql`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*