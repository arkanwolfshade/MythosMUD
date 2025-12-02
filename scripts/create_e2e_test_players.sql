-- Create test players for e2e testing
-- Password for both: Cthulhu1
-- Hash: $argon2id$v=19$m=65536,t=3,p=1$QboiqUn+9UiguuaKTN12HA$/mjnMcE390t4zRYqeK7xl/TTTK8VOCPytuSge+KSvug
-- ArkanWolfshade (Admin)
WITH arkan_user AS (
    INSERT INTO users (
            id,
            email,
            username,
            hashed_password,
            is_active,
            is_superuser,
            is_verified,
            created_at,
            updated_at
        )
    VALUES (
            gen_random_uuid(),
            'arkanwolfshade@test.local',
            'ArkanWolfshade',
            '$argon2id$v=19$m=65536,t=3,p=1$QboiqUn+9UiguuaKTN12HA$/mjnMcE390t4zRYqeK7xl/TTTK8VOCPytuSge+KSvug',
            true,
            false,
            true,
            NOW(),
            NOW()
        )
    RETURNING id
)
INSERT INTO players (
        player_id,
        user_id,
        name,
        stats,
        inventory,
        status_effects,
        current_room_id,
        experience_points,
        level,
        is_admin,
        created_at,
        last_active
    )
SELECT gen_random_uuid(),
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
FROM arkan_user u;
-- Ithaqua (Regular Player)
WITH ithaqua_user AS (
    INSERT INTO users (
            id,
            email,
            username,
            hashed_password,
            is_active,
            is_superuser,
            is_verified,
            created_at,
            updated_at
        )
    VALUES (
            gen_random_uuid(),
            'ithaqua@test.local',
            'Ithaqua',
            '$argon2id$v=19$m=65536,t=3,p=1$QboiqUn+9UiguuaKTN12HA$/mjnMcE390t4zRYqeK7xl/TTTK8VOCPytuSge+KSvug',
            true,
            false,
            true,
            NOW(),
            NOW()
        )
    RETURNING id
)
INSERT INTO players (
        player_id,
        user_id,
        name,
        stats,
        inventory,
        status_effects,
        current_room_id,
        experience_points,
        level,
        is_admin,
        created_at,
        last_active
    )
SELECT gen_random_uuid(),
    u.id,
    'Ithaqua',
    '{"health": 100, "sanity": 100, "strength": 10, "dexterity": 12, "constitution": 14, "intelligence": 10, "wisdom": 16, "charisma": 8, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "max_health": 100, "max_sanity": 100}'::jsonb,
    '[]'::jsonb,
    '[]'::jsonb,
    'earth_arkhamcity_sanitarium_room_foyer_001',
    0,
    1,
    0,
    NOW(),
    NOW()
FROM ithaqua_user u;
-- Ensure ArkanWolfshade has admin privileges
UPDATE players
SET is_admin = 1
WHERE name = 'ArkanWolfshade';
