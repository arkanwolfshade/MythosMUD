-- Verification checks for users and players migration
SET client_min_messages = WARNING;
SET search_path = public;

-- Basic row counts
SELECT
    (SELECT COUNT(*) FROM staging_users)  AS staging_users_count,
    (SELECT COUNT(*) FROM users)          AS users_count,
    (SELECT COUNT(*) FROM staging_players) AS staging_players_count,
    (SELECT COUNT(*) FROM players)         AS players_count;

-- Players without matching users (should be zero)
SELECT COUNT(*) AS players_without_users
FROM players p
LEFT JOIN users u ON u.id = p.user_id
WHERE u.id IS NULL;

-- id_map sanity checks
SELECT
    (SELECT COUNT(*) FROM id_map_users)   AS id_map_users_count,
    (SELECT COUNT(*) FROM id_map_players) AS id_map_players_count;

-- Sample data (first few rows)
SELECT id, username, is_admin, created_at FROM users ORDER BY created_at LIMIT 5;
SELECT id, name, sanity_score, created_at FROM players ORDER BY created_at LIMIT 5;
