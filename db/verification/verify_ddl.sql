-- Verification script to check if all required tables exist in the database
-- Run this against each database (mythos_dev, mythos_unit, mythos_e2e)

SET client_min_messages = WARNING;

-- Expected tables from schema files
DO $$
DECLARE
    expected_tables text[] := ARRAY[
        -- 01_world_and_calendar.sql
        'calendar_holidays',
        'calendar_npc_schedules',
        'emotes',
        'emote_aliases',
        'zones',
        'subzones',
        'rooms',
        'room_links',
        'aliases',
        -- 02_items_and_npcs.sql
        'item_component_states_static',
        'npc_definitions',
        'npc_relationships',
        'npc_spawn_rules',
        -- 03_identity_and_moderation.sql
        'professions',
        'muting_rules',
        'id_map_users',
        'id_map_players',
        -- 04_runtime_tables.sql
        'users',
        'players',
        'player_inventories',
        'invites',
        'player_sanity',
        'sanity_adjustment_log',
        'sanity_exposure_state',
        'sanity_cooldowns',
        'item_prototypes',
        'item_instances',
        'item_component_states'
    ];
    missing_tables text[] := '{}';
    table_name text;
BEGIN
    RAISE NOTICE 'Checking for required tables...';

    FOREACH table_name IN ARRAY expected_tables
    LOOP
        IF NOT EXISTS (
            SELECT 1
            FROM information_schema.tables AS t
            WHERE t.table_schema = 'public'
            AND t.table_name = table_name
        ) THEN
            missing_tables := array_append(missing_tables, table_name);
        END IF;
    END LOOP;

    IF array_length(missing_tables, 1) IS NULL THEN
        RAISE NOTICE 'SUCCESS: All required tables exist';
    ELSE
        RAISE WARNING 'MISSING TABLES: %', array_to_string(missing_tables, ', ');
    END IF;
END $$;

-- List all tables that exist
SELECT
    table_name,
    CASE
        WHEN table_name = ANY(ARRAY[
            'calendar_holidays',
            'calendar_npc_schedules',
            'emotes',
            'emote_aliases',
            'zones',
            'subzones',
            'rooms',
            'room_links',
            'aliases',
            'item_component_states_static',
            'npc_definitions',
            'npc_relationships',
            'npc_spawn_rules',
            'professions',
            'muting_rules',
            'id_map_users',
            'id_map_players',
            'users',
            'players',
            'player_inventories',
            'invites',
            'player_sanity',
            'sanity_adjustment_log',
            'sanity_exposure_state',
            'sanity_cooldowns',
            'item_prototypes',
            'item_instances',
            'item_component_states'
        ]) THEN 'Expected'
        ELSE 'Unexpected'
    END AS status
FROM information_schema.tables AS t
WHERE t.table_schema = 'public'
AND t.table_type = 'BASE TABLE'
ORDER BY status, table_name;
