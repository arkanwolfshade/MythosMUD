# users

> 8 nodes

## Key Concepts

- **users** (6 connections)
- **invites** (4 connections) — `db/schema.sql`
- **account_sanctions** (3 connections) — `db/schema.sql`
- **schema_name.reserve_invite()** (2 connections) — `db/procedures/players.sql`
- **get_user_id_by_username_ci()** (2 connections) — `db/schema.sql`
- **id_map_players** (2 connections) — `db/schema.sql`
- **muting_rules** (2 connections) — `db/schema.sql`
- **reserve_invite()** (2 connections) — `db/schema.sql`

## Relationships

- [schema.sql](schema.sql.md) (6 shared connections)
- [players](players.md) (2 shared connections)
- [players.sql](players.sql.md) (1 shared connections)

## Source Files

- `db/procedures/players.sql`
- `db/schema.sql`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*