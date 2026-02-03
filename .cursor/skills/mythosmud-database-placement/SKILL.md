---
name: mythosmud-database-placement
description: Enforce MythosMUD database placement: production under /data/players/ and /data/npcs/, tests under server/tests/data/players/ and server/tests/data/npcs/. PostgreSQL only; player_id is UUID. Use when creating or moving DB files, adding persistence, or discussing database paths.
---

# MythosMUD Database Placement

## Allowed Paths Only

| Environment | Player data | NPC data |
|-------------|-------------|----------|
| Production | `/data/players/` | `/data/npcs/` |
| Tests | `server/tests/data/players/` | `server/tests/data/npcs/` |

**Never** create database files outside these paths.

## Forbidden

- **Never** create files in `server/server/tests/data/players/`, `server/server/tests/data/npcs/`, or any other location.
- **Never** create `*.db` files without explicit permission. The project uses PostgreSQL, not SQLite.
- **Never** treat `player_id` as a string; it is a **UUID** type.

## Data Types

- **player_id:** UUID. Use the appropriate UUID type in PostgreSQL and in application code (e.g. Python `uuid.UUID`), not string.

## When Adding or Moving Persistence

1. Confirm which environment (production vs test).
2. Use only the paths in the table above.
3. Use PostgreSQL for persistence; do not introduce SQLite or new `*.db` files unless explicitly approved.
4. If you see database files in wrong locations, delete them and inform the user.

## Reference

- Full rules: [CLAUDE.md](../../CLAUDE.md) "CRITICAL DATABASE PLACEMENT RULES" and "Database Type Rules"
- Schema and DB docs: [db/README.md](../../db/README.md)
