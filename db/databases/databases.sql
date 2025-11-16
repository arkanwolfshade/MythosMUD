-- MythosMUD PostgreSQL Databases Provisioning
-- Run connected to a superuser on the 'postgres' database.
-- Creates three databases and enables pgcrypto in each, with secure defaults.
-- Applies least-privilege grants to application roles.

-- Create databases with owners (must not run inside a transaction/function)
SELECT 'CREATE DATABASE mythos_dev OWNER mythos_owner_dev ENCODING ''UTF8'' TEMPLATE template1'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mythos_dev')\gexec

SELECT 'CREATE DATABASE mythos_unit OWNER mythos_owner_unit ENCODING ''UTF8'' TEMPLATE template1'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mythos_unit')\gexec

SELECT 'CREATE DATABASE mythos_e2e OWNER mythos_owner_e2e ENCODING ''UTF8'' TEMPLATE template1'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mythos_e2e')\gexec

\connect mythos_dev
SET client_min_messages = WARNING;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
-- Secure schema defaults
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE mythos_dev FROM PUBLIC;
GRANT CONNECT ON DATABASE mythos_dev TO mythos_app_dev;
GRANT USAGE ON SCHEMA public TO mythos_app_dev;
-- Default privileges: tables/sequences/functions to app role
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_dev IN SCHEMA public
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO mythos_app_dev;
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_dev IN SCHEMA public
    GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO mythos_app_dev;
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_dev IN SCHEMA public
    GRANT EXECUTE ON FUNCTIONS TO mythos_app_dev;
-- Enforce UTC
ALTER DATABASE mythos_dev SET timezone TO 'UTC';

\connect mythos_unit
SET client_min_messages = WARNING;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE mythos_unit FROM PUBLIC;
GRANT CONNECT ON DATABASE mythos_unit TO mythos_app_unit;
GRANT USAGE ON SCHEMA public TO mythos_app_unit;
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_unit IN SCHEMA public
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO mythos_app_unit;
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_unit IN SCHEMA public
    GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO mythos_app_unit;
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_unit IN SCHEMA public
    GRANT EXECUTE ON FUNCTIONS TO mythos_app_unit;
ALTER DATABASE mythos_unit SET timezone TO 'UTC';

\connect mythos_e2e
SET client_min_messages = WARNING;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE mythos_e2e FROM PUBLIC;
GRANT CONNECT ON DATABASE mythos_e2e TO mythos_app_e2e;
GRANT USAGE ON SCHEMA public TO mythos_app_e2e;
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_e2e IN SCHEMA public
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO mythos_app_e2e;
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_e2e IN SCHEMA public
    GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO mythos_app_e2e;
ALTER DEFAULT PRIVILEGES FOR ROLE mythos_owner_e2e IN SCHEMA public
    GRANT EXECUTE ON FUNCTIONS TO mythos_app_e2e;
ALTER DATABASE mythos_e2e SET timezone TO 'UTC';
