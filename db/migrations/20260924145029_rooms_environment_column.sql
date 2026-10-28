-- #663: promote rooms.environment out of the attributes JSONB blob into a typed column,
-- consistent with zones.environment / subzones.environment (chk_zones_environment /
-- chk_subzones_environment). Replaces the expression CHECK added by #623
-- (chk_rooms_environment, over attributes->>'environment').
--
-- DDL half. The data half, which backfills the column from the JSONB key, is
-- data/db/migrations/20260924145030_rooms_environment_backfill.sql and runs right after this one.
--
-- Idempotent: safe to run against a database that already has the column (fresh baseline +
-- replay), and against mythos_dev. Re-running it on a database that applied the pre-split migration is harmless.

-- migrate:up
ALTER TABLE rooms ADD COLUMN IF NOT EXISTS environment text;

ALTER TABLE rooms DROP CONSTRAINT IF EXISTS chk_rooms_environment;

ALTER TABLE rooms ADD CONSTRAINT chk_rooms_environment
    CHECK (environment IS NULL OR environment = ANY(ARRAY[
        'indoors', 'outdoors', 'underwater', 'intersection', 'street_paved', 'arena', 'void'
    ]));

COMMENT ON COLUMN rooms.environment IS
    'Room-specific environment override. NULL means "inherit from subzone, then zone, then '
    'outdoors" -- see get_rooms_with_exits()''s resolved_environment. Matches '
    'zones.environment / subzones.environment (#663).';

-- migrate:down
ALTER TABLE rooms DROP CONSTRAINT IF EXISTS chk_rooms_environment;

ALTER TABLE rooms ADD CONSTRAINT chk_rooms_environment
    CHECK ((((attributes ->> 'environment'::text) IS NULL) OR ((attributes ->> 'environment'::text) = ANY(ARRAY[
        'indoors'::text, 'outdoors'::text, 'underwater'::text, 'intersection'::text,
        'street_paved'::text, 'arena'::text, 'void'::text
    ]))));

ALTER TABLE rooms DROP COLUMN IF EXISTS environment;
