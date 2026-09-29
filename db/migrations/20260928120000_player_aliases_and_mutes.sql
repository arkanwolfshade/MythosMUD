-- #680 / #681: move player command aliases and player mutes out of per-player JSON files
-- (data/<env>/aliases/*_aliases.json, data/<env>/user_management/mutes_*.json) into PostgreSQL.
-- Legacy JSON data is intentionally not imported.
--
-- Both tables key on players.player_id (not name), so a soft-deleted character's rows can never
-- leak to a new character that later reuses the name.
--
-- Idempotent: safe to replay against a database that already has these tables.

-- migrate:up
CREATE TABLE IF NOT EXISTS player_aliases (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    player_id uuid NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
    -- `name` mirrors players.name; RF04 flags it as a keyword.
    name varchar(20) NOT NULL, -- noqa: RF04
    command varchar(200) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_player_aliases_player_lower_name
    ON player_aliases (player_id, lower(name));

CREATE TABLE IF NOT EXISTS player_mutes (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    mute_type text NOT NULL,
    muter_id uuid NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
    muter_name varchar(50) NOT NULL,
    target_id uuid REFERENCES players (player_id) ON DELETE CASCADE,
    target_name varchar(50),
    channel varchar(32),
    reason text NOT NULL DEFAULT '',
    muted_at timestamptz NOT NULL DEFAULT now(),
    expires_at timestamptz,
    CONSTRAINT chk_player_mutes_type CHECK (mute_type IN ('player', 'channel', 'global')),
    -- channel mutes name a channel and no target; player/global mutes name a target and no channel
    CONSTRAINT chk_player_mutes_shape CHECK (
        (mute_type = 'channel' AND channel IS NOT NULL AND target_id IS NULL)
        OR (mute_type <> 'channel' AND channel IS NULL AND target_id IS NOT NULL)
    )
);

COMMENT ON COLUMN player_mutes.expires_at IS 'NULL means permanent.';

CREATE UNIQUE INDEX IF NOT EXISTS idx_player_mutes_player
    ON player_mutes (muter_id, target_id) WHERE mute_type = 'player';
CREATE UNIQUE INDEX IF NOT EXISTS idx_player_mutes_channel
    ON player_mutes (muter_id, channel) WHERE mute_type = 'channel';
CREATE UNIQUE INDEX IF NOT EXISTS idx_player_mutes_global
    ON player_mutes (target_id) WHERE mute_type = 'global';

-- migrate:down
DROP TABLE IF EXISTS player_mutes;
DROP TABLE IF EXISTS player_aliases;
