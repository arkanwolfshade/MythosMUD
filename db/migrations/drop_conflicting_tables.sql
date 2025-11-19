-- Drop tables that conflict with SQLAlchemy model definitions
-- These tables will be recreated by SQLAlchemy via metadata.create_all()
-- with the correct schema matching the models.

SET client_min_messages = WARNING;
SET search_path = public;

-- Drop runtime tables that SQLAlchemy will recreate with correct schema
-- Drop in dependency order to avoid foreign key constraint errors

-- Drop sanity tables first (depend on players)
DROP TABLE IF EXISTS sanity_cooldowns CASCADE;
DROP TABLE IF EXISTS sanity_exposure_state CASCADE;
DROP TABLE IF EXISTS sanity_adjustment_log CASCADE;
DROP TABLE IF EXISTS player_sanity CASCADE;

-- Drop item tables (depend on item_prototypes)
DROP TABLE IF EXISTS item_component_states CASCADE;
DROP TABLE IF EXISTS item_instances CASCADE;
DROP TABLE IF EXISTS item_prototype_component_defaults CASCADE;
DROP TABLE IF EXISTS item_prototypes CASCADE;

-- Drop players (depends on users and professions)
DROP TABLE IF EXISTS players CASCADE;

-- Drop users (SQLAlchemy will recreate with correct FastAPI Users schema)
-- NOTE: This will lose data - only run on test databases!
DROP TABLE IF EXISTS users CASCADE;

-- Drop invites (depends on users)
DROP TABLE IF EXISTS invites CASCADE;

-- Note: We keep the static data tables (rooms, zones, npc_definitions, professions, etc.)
-- and let SQLAlchemy create the runtime tables with the correct schema
