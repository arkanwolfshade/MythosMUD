SET client_min_messages = WARNING;
SET search_path = public;

-- Basic row counts
SELECT 'staging_users' AS table_name, COUNT(*) AS row_count FROM staging_users
UNION ALL
SELECT 'staging_players', COUNT(*) FROM staging_players
UNION ALL
SELECT 'users', COUNT(*) FROM users
UNION ALL
SELECT 'players', COUNT(*) FROM players
UNION ALL
SELECT 'id_map_users', COUNT(*) FROM id_map_users
UNION ALL
SELECT 'id_map_players', COUNT(*) FROM id_map_players;

-- Check that every staging user has an id_map and users row
SELECT 'missing_id_map_for_user' AS check_name, COUNT(*) AS problem_rows
FROM staging_users s
LEFT JOIN id_map_users m ON m.old_sqlite_id = s.old_sqlite_id
WHERE m.old_sqlite_id IS NULL;

SELECT 'missing_loaded_user' AS check_name, COUNT(*) AS problem_rows
FROM id_map_users m
LEFT JOIN users u ON u.id = m.new_uuid
WHERE u.id IS NULL;

-- Check that every staging player has an id_map and players row
SELECT 'missing_id_map_for_player' AS check_name, COUNT(*) AS problem_rows
FROM staging_players s
LEFT JOIN id_map_players m ON m.old_sqlite_id = s.old_sqlite_id
WHERE m.old_sqlite_id IS NULL;

SELECT 'missing_loaded_player' AS check_name, COUNT(*) AS problem_rows
FROM id_map_players m
LEFT JOIN players p ON p.id = m.new_uuid
WHERE p.id IS NULL;

-- FK sanity: players.user_id must exist in users.id
SELECT 'orphan_player_user_fk' AS check_name, COUNT(*) AS problem_rows
FROM players p
LEFT JOIN users u ON u.id = p.user_id
WHERE u.id IS NULL;
