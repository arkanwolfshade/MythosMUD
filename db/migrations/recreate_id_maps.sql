SET client_min_messages = WARNING;
SET search_path = public;

DROP TABLE IF EXISTS id_map_players CASCADE;
DROP TABLE IF EXISTS id_map_users CASCADE;

-- Recreate from canonical schema
-- NOTE: This migration script references legacy schema files.
-- The authoritative schema is now in db/authoritative_schema.sql
-- This script may need updating if the id_maps table structure changes.
