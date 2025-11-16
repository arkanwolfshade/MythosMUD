-- MythosMUD PostgreSQL Roles
-- Apply with a superuser connection (e.g., psql to 'postgres' DB).
-- This script creates owner roles (no login) and application roles (no login).
-- Create actual login users separately and GRANT them membership in the app roles.
-- Security rationale: ownership is separated from day-to-day application privileges.

-- Owners (no login)
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'mythos_owner_dev') THEN
        CREATE ROLE mythos_owner_dev NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'mythos_owner_unit') THEN
        CREATE ROLE mythos_owner_unit NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'mythos_owner_e2e') THEN
        CREATE ROLE mythos_owner_e2e NOLOGIN;
    END IF;
END$$;

-- Application roles (no login)
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'mythos_app_dev') THEN
        CREATE ROLE mythos_app_dev NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'mythos_app_unit') THEN
        CREATE ROLE mythos_app_unit NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'mythos_app_e2e') THEN
        CREATE ROLE mythos_app_e2e NOLOGIN;
    END IF;
END$$;

-- Example (commented) for creating a login and assigning it to an app role:
-- CREATE ROLE mythos_app_dev_user LOGIN PASSWORD 'use_env_managed_secret';
-- GRANT mythos_app_dev TO mythos_app_dev_user;
