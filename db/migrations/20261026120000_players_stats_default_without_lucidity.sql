-- Lucidity leaves players.stats (ADR-029 step 3a): the schema half.
--
-- Lucidity lives only in player_lucidity.current_lcd. New rows stop getting a stats.lucidity key from the column
-- default. The data half, data/db/migrations/20261026120001_lucidity_single_store.sql, runs right after this one:
-- it backfills player_lucidity for players who never had a row, then removes the key from existing rows.
-- Idempotent: safe to replay.

-- migrate:up
ALTER TABLE players ALTER COLUMN stats SET DEFAULT jsonb_build_object(
    'luck', 50, 'size', 50, 'power', 50, 'occult', 0, 'charisma', 50, 'position', 'standing',
    'strength', 50, 'dexterity', 50, 'education', 50, 'corruption', 0, 'current_dp', 20,
    'constitution', 50, 'intelligence', 50, 'magic_points', 10
);

-- migrate:down
ALTER TABLE players ALTER COLUMN stats SET DEFAULT jsonb_build_object(
    'luck', 50, 'size', 50, 'power', 50, 'occult', 0, 'charisma', 50, 'lucidity', 100, 'position', 'standing',
    'strength', 50, 'dexterity', 50, 'education', 50, 'corruption', 0, 'current_dp', 20,
    'constitution', 50, 'intelligence', 50, 'magic_points', 10
);
