-- Baseline marker (#811).
--
-- dbmate cannot run with zero migration files present, and every schema/seed change up to this
-- point is already captured in db/schema.sql and data/db/seed.sql -- loaded once, outside dbmate,
-- when a database is first provisioned (see db/databases/databases.sql and
-- scripts/load_world_seed.py). This file exists only to give dbmate a first entry in
-- schema_migrations so `dbmate up`/`status` has something to track; it makes no schema change.
--
-- Real migrations start after this one.

-- migrate:up
SELECT 1;

-- migrate:down
SELECT 1;
