-- Staging tables for runtime data extracted from SQLite
-- Load order: create staging tables, \copy CSVs, then run transform script.

SET client_min_messages = WARNING;
SET search_path = public;

CREATE TABLE IF NOT EXISTS staging_users (
	old_sqlite_id	text PRIMARY KEY, -- UUID string from SQLite
	username		text,
	email			text,
	hashed_password	text,
	is_active		boolean,
	is_superuser	boolean,
	is_verified		boolean,
	created_at		timestamptz,
	updated_at		timestamptz
);

CREATE TABLE IF NOT EXISTS staging_players (
	old_sqlite_id	text PRIMARY KEY, -- player_id (UUID string)
	user_id			text,            -- users.id (UUID string)
	name			text,
	is_admin		boolean,
	profession_sqlite_id integer,
	stats_json		text,
	inventory_json	text,
	status_effects_json text,
	current_room_id text,
	respawn_room_id text,
	experience_points integer,
	level			integer,
	created_at		timestamptz,
	last_active		timestamptz
);

-- Optional additional staging tables can be added here as needed (sanity logs, etc.)
