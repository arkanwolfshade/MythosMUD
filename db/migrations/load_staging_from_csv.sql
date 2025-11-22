\
set ON_ERROR_STOP on
SET client_min_messages = WARNING;
SET search_path = public;
-- Historical migration script: Loads CSV data from staging
-- NOTE: CSV files have been moved to data/db/migrations/
-- Update the FROM paths below to use absolute paths or copy files to the PostgreSQL server's accessible location
-- Original location: data/migration/csv/*.csv
\ copy staging_users (
    old_sqlite_id,
    email,
    username,
    hashed_password,
    is_active,
    is_superuser,
    is_verified,
    created_at,
    updated_at
)
FROM 'data/db/migrations/users.csv' WITH (FORMAT csv, HEADER true) \ copy staging_players (
        old_sqlite_id,
        user_id,
        name,
        is_admin,
        profession_sqlite_id,
        stats_json,
        inventory_json,
        status_effects_json,
        current_room_id,
        respawn_room_id,
        experience_points,
        level,
        created_at,
        last_active
    )
FROM 'data/db/migrations/players.csv' WITH (FORMAT csv, HEADER true)
