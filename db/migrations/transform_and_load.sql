\set ON_ERROR_STOP on
SET client_min_messages = WARNING;
SET search_path = public;

-- Populate users with v4 UUIDs and create id_map_users
INSERT INTO id_map_users (old_sqlite_id, new_uuid, username)
SELECT s.old_sqlite_id, gen_random_uuid(), s.username
FROM staging_users s
ON CONFLICT (old_sqlite_id) DO NOTHING;

INSERT INTO users (id, username, display_name, email, password_hash, is_admin, created_at, updated_at)
SELECT m.new_uuid,
	   s.username,
	   s.username AS display_name,
	   s.email,
	   s.hashed_password AS password_hash,
	   COALESCE(s.is_superuser,false) AS is_admin,
	   COALESCE(s.created_at, now()),
	   COALESCE(s.updated_at, now())
FROM staging_users s
JOIN id_map_users m ON m.old_sqlite_id = s.old_sqlite_id
ON CONFLICT (username) DO NOTHING;

-- Populate players with v4 UUIDs and create id_map_players
INSERT INTO id_map_players (old_sqlite_id, new_uuid, user_uuid, name)
SELECT s.old_sqlite_id, gen_random_uuid(), u.id, s.name
FROM staging_players s
JOIN id_map_users mu ON mu.old_sqlite_id = s.user_id
JOIN users u ON u.id = mu.new_uuid
ON CONFLICT (old_sqlite_id) DO NOTHING;

INSERT INTO players (id, user_id, name, profession_id, sanity_score, attributes, created_at, updated_at)
SELECT mp.new_uuid,
	   mu.new_uuid AS user_id,
	   s.name,
	   NULL::uuid AS profession_id,
	   COALESCE((s.stats_json::jsonb ->> 'sanity')::int, 100) AS sanity_score,
	   jsonb_build_object(
		   'stats', COALESCE(NULLIF(s.stats_json,'')::jsonb, '{}'::jsonb),
		   'inventory', COALESCE(NULLIF(s.inventory_json,'')::jsonb, '[]'::jsonb),
		   'status_effects', COALESCE(NULLIF(s.status_effects_json,'')::jsonb, '[]'::jsonb),
		   'current_room_id', s.current_room_id,
		   'respawn_room_id', s.respawn_room_id,
		   'experience_points', s.experience_points,
		   'level', s.level,
		   'is_admin', s.is_admin
	   ) AS attributes,
	   COALESCE(s.created_at, now()),
	   COALESCE(s.last_active, now())
FROM staging_players s
JOIN id_map_players mp ON mp.old_sqlite_id = s.old_sqlite_id
JOIN id_map_users mu ON mu.old_sqlite_id = s.user_id
ON CONFLICT (name) DO NOTHING;
