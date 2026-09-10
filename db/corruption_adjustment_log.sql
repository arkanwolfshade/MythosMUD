-- Corruption ledger and cooldown tables (#804, #145).
--
-- These are NOT applied via db/procedures/ (that directory is for stored procedures/functions,
-- reapplied idempotently on every apply_procedures.ps1 run; these are plain tables, applied
-- once). Structural mirror of lucidity_adjustment_log / lucidity_cooldowns
-- (see db/mythos_dev_ddl.sql).
--
-- Apply with the target database's own schema as search_path, e.g.:
--   psql -h localhost -U postgres -d mythos_dev -v schema_name=mythos_dev -f db/corruption_adjustment_log.sql
--
-- After applying to mythos_dev/mythos_unit/mythos_e2e, regenerate the authoritative DDL dumps:
--   scripts/generate_schema_from_dev.ps1 (then remove SET transaction_timeout if present, per its
--   own header instructions) and commit the updated db/mythos_*_ddl.sql files. This file itself is
--   not the source of truth after that -- the regenerated dumps are.

SET search_path = :schema_name; -- noqa: PRS,LT01

CREATE TABLE IF NOT EXISTS corruption_adjustment_log (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    player_id UUID NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
    delta INTEGER NOT NULL,
    reason_code TEXT NOT NULL,
    metadata TEXT NOT NULL DEFAULT '{}',
    location_id VARCHAR(255),
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now()
);

COMMENT ON TABLE corruption_adjustment_log IS 'Immutable ledger for every corruption gain or loss event.';

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_corruption_adjustment_player_created
    ON corruption_adjustment_log (player_id, created_at);

CREATE TABLE IF NOT EXISTS corruption_cooldowns (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    player_id UUID NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
    action_code TEXT NOT NULL,
    cooldown_expires_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    CONSTRAINT uq_corruption_cooldown_player_action UNIQUE (player_id, action_code)
);

COMMENT ON TABLE corruption_cooldowns IS 'Cooldown tracker for corruption recovery rites (e.g. /cleanse).';
