# 📋 Test Coverage Breakdown

> 8 nodes · cohesion 0.25

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

- [test_connection_delegates.py](test_connection_delegates.py.md) (6 shared connections)
- [packages/README.md](packages-README.md.md) (2 shared connections)
- [test_ascii_map_exits.py](test_ascii_map_exits.py.md) (1 shared connections)

## Source Files

- `db/procedures/players.sql`
- `db/schema.sql`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*