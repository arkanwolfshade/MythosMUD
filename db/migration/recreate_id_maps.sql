SET client_min_messages = WARNING;
SET search_path = public;

DROP TABLE IF EXISTS id_map_players CASCADE;
DROP TABLE IF EXISTS id_map_users CASCADE;

-- Recreate from canonical schema
\i db/schema/03_identity_and_moderation.sql
