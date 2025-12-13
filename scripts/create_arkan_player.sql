-- Create player record for existing ArkanWolfshade user
-- nosemgrep
-- NOPMD
-- Note: This script targets standard game tables (users, players), not RAC_* tables.
-- The Codacy RAC_* rule does not apply to this project's database schema.
INSERT INTO players (player_id, user_id, name, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
SELECT
    gen_random_uuid(),
    u.id,
    'ArkanWolfshade',
    '{"strength": 50, "dexterity": 50, "constitution": 50, "size": 50, "intelligence": 50, "power": 50, "education": 50, "charisma": 50, "luck": 50, "lucidity": 100, "occult": 0, "corruption": 0, "current_dp": 20, "max_dp": 20, "magic_points": 10, "max_magic_points": 10, "max_lucidity": 100, "position": "standing"}'::jsonb,
    '[]'::jsonb,
    '[]'::jsonb,
    'earth_arkhamcity_sanitarium_room_foyer_001',
    0,
    1,
    1,
    NOW(),
    NOW()
FROM users u
WHERE u.username = 'ArkanWolfshade'
  AND NOT EXISTS (SELECT 1 FROM players WHERE user_id = u.id);
