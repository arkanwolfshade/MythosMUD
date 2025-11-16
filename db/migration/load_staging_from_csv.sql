\
set ON_ERROR_STOP on
SET client_min_messages = WARNING;
SET search_path = public;
-- Assumes CSVs exist in data/migration/csv/*.csv with headers
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
FROM 'data/migration/csv/users.csv' WITH (FORMAT csv, HEADER true) \ copy staging_players (
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
FROM 'data/migration/csv/players.csv' WITH (FORMAT csv, HEADER true)
