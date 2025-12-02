-- Create player record for existing ArkanWolfshade user
INSERT INTO players (player_id, user_id, name, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
SELECT
    gen_random_uuid(),
    u.id,
    'ArkanWolfshade',
    '{"health": 100, "sanity": 100, "strength": 12, "dexterity": 14, "constitution": 10, "intelligence": 16, "wisdom": 8, "charisma": 10, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "max_health": 100, "max_sanity": 100}'::jsonb,
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
