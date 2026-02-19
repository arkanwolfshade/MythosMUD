-- Migration: PostgreSQL Anti-Patterns Fixes
-- Description: Fixes critical PostgreSQL best practices violations:
--   - Convert serial/SERIAL to bigint generated always as identity
--   - Convert INTEGER primary keys to bigint generated always as identity
--   - Convert unnecessary varchar(n) to text
--   - Add table and column comments
--   - Standardize SQL formatting to lowercase
-- Date: 2025-01-14
--
-- WARNING: This migration modifies existing table structures.
-- Test thoroughly in development before applying to production.
--
-- Tables affected:
--   - lucidity_adjustment_log (id: serial -> bigint generated always as identity)
--   - lucidity_exposure_state (id: serial -> bigint generated always as identity)
--   - lucidity_cooldowns (id: serial -> bigint generated always as identity)
--   - item_component_states (id: serial -> bigint generated always as identity)
--   - npc_definitions (id: SERIAL -> bigint generated always as identity)
--   - npc_spawn_rules (id: SERIAL -> bigint generated always as identity)
--   - npc_relationships (id: SERIAL -> bigint generated always as identity)
--   - player_spells (id: SERIAL -> bigint generated always as identity)
--   - professions (id: SERIAL -> bigint generated always as identity)

set client_min_messages = warning;
set search_path = public;

-- ============================================================================
-- Helper function to convert serial column to identity
-- ============================================================================
-- This function safely converts a serial column to bigint generated always as identity
-- by preserving the current sequence value and dropping the old sequence.
create or replace function convert_serial_to_identity(
    table_name text,
    column_name text,
    sequence_name text
) returns void as $$
declare
    current_val bigint;
begin
    -- Get current sequence value (or 1 if sequence doesn't exist)
    begin
        execute format('select coalesce(last_value, 1) from %I', sequence_name) into current_val;
    exception
        when others then
            current_val := 1;
    end;

    -- Drop default from column
    execute format('alter table %I alter column %I drop default', table_name, column_name);

    -- Drop sequence ownership (if exists)
    begin
        execute format('alter sequence %I owned by none', sequence_name);
    exception
        when others then
            -- Sequence might not exist or already be dropped, continue
            null;
    end;

    -- Convert column to identity
    execute format(
        'alter table %I alter column %I type bigint, alter column %I add generated always as identity',
        table_name, column_name, column_name
    );

    -- Set identity to start from current value + 1
    execute format(
        'alter table %I alter column %I restart with %s',
        table_name, column_name, current_val + 1
    );

    -- Drop the old sequence (if it still exists)
    begin
        execute format('drop sequence if exists %I', sequence_name);
    exception
        when others then
            -- Sequence might already be dropped, continue
            null;
    end;
end;
$$ language plpgsql;

-- ============================================================================
-- Convert serial columns to bigint generated always as identity
-- ============================================================================

-- lucidity_adjustment_log.id
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'lucidity_adjustment_log'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        perform convert_serial_to_identity(
            'lucidity_adjustment_log',
            'id',
            'sanity_adjustment_log_id_seq'
        );
    end if;
end $$;

-- lucidity_exposure_state.id
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'lucidity_exposure_state'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        perform convert_serial_to_identity(
            'lucidity_exposure_state',
            'id',
            'sanity_exposure_state_id_seq'
        );
    end if;
end $$;

-- lucidity_cooldowns.id
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'lucidity_cooldowns'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        perform convert_serial_to_identity(
            'lucidity_cooldowns',
            'id',
            'sanity_cooldowns_id_seq'
        );
    end if;
end $$;

-- item_component_states.id
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'item_component_states'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        perform convert_serial_to_identity(
            'item_component_states',
            'id',
            'item_component_states_id_seq'
        );
    end if;
end $$;

-- npc_definitions.id
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'npc_definitions'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        perform convert_serial_to_identity(
            'npc_definitions',
            'id',
            'npc_definitions_id_seq'
        );
    end if;
end $$;

-- npc_spawn_rules.id
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'npc_spawn_rules'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        perform convert_serial_to_identity(
            'npc_spawn_rules',
            'id',
            'npc_spawn_rules_id_seq'
        );
    end if;
end $$;

-- npc_relationships.id
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'npc_relationships'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        perform convert_serial_to_identity(
            'npc_relationships',
            'id',
            'npc_relationships_id_seq'
        );
    end if;
end $$;

-- player_spells.id
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'player_spells'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        perform convert_serial_to_identity(
            'player_spells',
            'id',
            'player_spells_id_seq'
        );
    end if;
end $$;

-- professions.id
-- Note: professions.id is INTEGER PRIMARY KEY (not serial), so we need special handling
do $$
declare
    current_max bigint;
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'professions'
        and column_name = 'id'
        and data_type = 'integer'
    ) then
        -- Get current max ID value
        -- nosemgrep: Semgrep_codacy.generic.sql.rac-table-access
        -- This migration script queries the professions game table to determine the current max ID
        -- before converting the column type. RAC_* table wrappers are not used in this schema,
        -- so the generic RAC_* enforcement rule does not apply here.
        select coalesce(max(id), 0) into current_max from professions;

        -- Drop default if it exists (needed before adding identity)
        -- Check if column has a default value
        if exists (
            select 1
            from information_schema.columns
            where table_schema = 'public'
            and table_name = 'professions'
            and column_name = 'id'
            and column_default is not null
        ) then
            alter table professions alter column id drop default;
        end if;

        -- Convert to bigint first
        alter table professions alter column id type bigint;

        -- Add identity (if not already identity)
        if not exists (
            select 1
            from information_schema.columns
            where table_schema = 'public'
            and table_name = 'professions'
            and column_name = 'id'
            and is_identity = 'YES'
        ) then
            alter table professions alter column id add generated always as identity;
            -- Set restart value using dynamic SQL since RESTART WITH doesn't accept expressions
            execute format('alter table professions alter column id restart with %s', current_max + 1);
        end if;

        -- Drop sequence if it exists
        drop sequence if exists professions_id_seq;
    end if;
end $$;

-- ============================================================================
-- Update foreign key columns to match new bigint primary keys
-- ============================================================================

-- npc_spawn_rules.npc_definition_id: integer -> bigint
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'npc_spawn_rules'
        and column_name = 'npc_definition_id'
        and data_type = 'integer'
    ) then
        alter table npc_spawn_rules alter column npc_definition_id type bigint;
    end if;
end $$;

-- npc_relationships.npc_id_1: integer -> bigint
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'npc_relationships'
        and column_name = 'npc_id_1'
        and data_type = 'integer'
    ) then
        alter table npc_relationships alter column npc_id_1 type bigint;
    end if;
end $$;

-- npc_relationships.npc_id_2: integer -> bigint
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'npc_relationships'
        and column_name = 'npc_id_2'
        and data_type = 'integer'
    ) then
        alter table npc_relationships alter column npc_id_2 type bigint;
    end if;
end $$;

-- players.profession_id: integer -> bigint
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'players'
        and column_name = 'profession_id'
        and data_type = 'integer'
    ) then
        alter table players alter column profession_id type bigint;
    end if;
end $$;

-- ============================================================================
-- Convert unnecessary varchar(n) to text
-- ============================================================================
-- Note: Only converting columns where length constraints are not business-critical
-- Keeping varchar for columns where length limits are meaningful (e.g., codes, IDs)

-- users.email: varchar(255) -> text
-- Note: Keeping as varchar if there's a business requirement for email length
-- Uncomment if email length constraint is not needed:
-- alter table users alter column email type text;

-- users.username: varchar(255) -> text
-- Note: Keeping as varchar if there's a business requirement for username length
-- Uncomment if username length constraint is not needed:
-- alter table users alter column username type text;

-- users.display_name: varchar(255) -> text
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'users'
        and column_name = 'display_name'
        and data_type = 'character varying'
    ) then
        alter table users alter column display_name type text;
    end if;
end $$;

-- users.password_hash: varchar(255) -> text
do $$
begin
    if exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'users'
        and column_name = 'password_hash'
        and data_type = 'character varying'
    ) then
        alter table users alter column password_hash type text;
    end if;
end $$;

-- invites.invite_code: varchar(255) -> text
-- Note: Keeping as varchar if invite codes have fixed length requirements
-- Uncomment if invite code length constraint is not needed:
-- alter table invites alter column invite_code type text;

-- player_lucidity.current_tier: varchar(32) -> text
-- Note: Keeping as varchar since it's a fixed enum value with small length
-- This is acceptable as the length constraint is meaningful

-- lucidity_adjustment_log.reason_code: varchar(64) -> text
do $$
begin
    if exists (
        select 1
        from information_schema.tables
        where table_schema = 'public'
        and table_name = 'lucidity_adjustment_log'
    ) and exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'lucidity_adjustment_log'
        and column_name = 'reason_code'
        and data_type = 'character varying'
    ) then
        alter table lucidity_adjustment_log alter column reason_code type text;
    end if;
end $$;

-- lucidity_exposure_state.entity_archetype: varchar(128) -> text
do $$
begin
    if exists (
        select 1
        from information_schema.tables
        where table_schema = 'public'
        and table_name = 'lucidity_exposure_state'
    ) and exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'lucidity_exposure_state'
        and column_name = 'entity_archetype'
        and data_type = 'character varying'
    ) then
        alter table lucidity_exposure_state alter column entity_archetype type text;
    end if;
end $$;

-- lucidity_cooldowns.action_code: varchar(64) -> text
do $$
begin
    if exists (
        select 1
        from information_schema.tables
        where table_schema = 'public'
        and table_name = 'lucidity_cooldowns'
    ) and exists (
        select 1
        from information_schema.columns
        where table_schema = 'public'
        and table_name = 'lucidity_cooldowns'
        and column_name = 'action_code'
        and data_type = 'character varying'
    ) then
        alter table lucidity_cooldowns alter column action_code type text;
    end if;
end $$;

-- ============================================================================
-- Add table and column comments
-- ============================================================================

-- Table comments
comment on table users is 'Stores user account information for authentication and authorization.';
comment on table players is 'Stores runtime game data for player characters.';
comment on table player_inventories is 'Stores JSON payloads for player inventory and equipped items.';
comment on table invites is 'Manages invite-only registration system with expiration tracking.';
comment on table player_lucidity is 'Tracks player lucidity (sanity) state and tier.';
do $$
begin
    -- nosemgrep: Semgrep_codacy.generic.sql.rac-table-access
    -- This queries information_schema (metadata), not application data tables.
    -- The RAC rule applies to SELECT/INSERT/UPDATE/DELETE queries on data tables,
    -- not to metadata queries checking table existence.
    if exists (select 1 from information_schema.tables where table_schema = 'public' and table_name = 'lucidity_adjustment_log') then
        comment on table lucidity_adjustment_log is 'Immutable ledger for every lucidity gain or loss event.';
    end if;
    if exists (select 1 from information_schema.tables where table_schema = 'public' and table_name = 'lucidity_exposure_state') then
        comment on table lucidity_exposure_state is 'Tracks repeated exposure to particular eldritch archetypes.';
    end if;
    if exists (select 1 from information_schema.tables where table_schema = 'public' and table_name = 'lucidity_cooldowns') then
        comment on table lucidity_cooldowns is 'Cooldown tracker for recovery rituals and hallucination timers.';
    end if;
end $$;
comment on table item_prototypes is 'Static reference data for item types and their properties.';
comment on table item_instances is 'Runtime instances of items in the game world.';
comment on table item_component_states is 'Component-specific state data for item instances.';
comment on table npc_definitions is 'Static reference data for NPC types and their configurations.';
comment on table npc_spawn_rules is 'Rules governing NPC spawning behavior in subzones.';
comment on table npc_relationships is 'Relationship mappings between NPCs (ally, enemy, neutral, follower).';
comment on table professions is 'Static reference data for character professions and their requirements.';
comment on table player_spells is 'Tracks spells learned by players and their mastery levels.';
comment on table spells is 'Global spell registry with spell definitions and properties.';
comment on table muting_rules is 'Admin moderation rules for muting users or players.';

-- Column comments for critical columns
comment on column users.id is 'Primary key: UUID generated automatically.';
comment on column users.email is 'User email address (must be unique).';
comment on column users.username is 'User login name (must be unique).';
comment on column players.player_id is 'Primary key: Unique identifier for the player character.';
comment on column players.user_id is 'Foreign key to users table. Links player to user account.';
comment on column players.name is 'Character name (must be unique, case-sensitive).';
comment on column players.stats is 'JSON object containing character statistics (strength, dexterity, etc.).';
comment on column players.inventory is 'JSON array of inventory items.';
comment on column players.status_effects is 'JSON array of active status effects.';
do $$
begin
    if exists (select 1 from information_schema.columns where table_schema = 'public' and table_name = 'player_lucidity' and column_name = 'current_lcd') then
        comment on column player_lucidity.current_lcd is 'Current lucidity value (-100 to +100).';
    end if;
end $$;
do $$
begin
    if exists (select 1 from information_schema.columns where table_schema = 'public' and table_name = 'player_lucidity' and column_name = 'current_tier') then
        comment on column player_lucidity.current_tier is 'Current lucidity tier: lucid, uneasy, fractured, deranged, or catatonic.';
    end if;
end $$;
do $$
begin
    if exists (select 1 from information_schema.columns where table_schema = 'public' and table_name = 'lucidity_adjustment_log' and column_name = 'delta') then
        comment on column lucidity_adjustment_log.delta is 'Change in lucidity value (positive for gain, negative for loss).';
    end if;
    if exists (select 1 from information_schema.columns where table_schema = 'public' and table_name = 'lucidity_adjustment_log' and column_name = 'reason_code') then
        comment on column lucidity_adjustment_log.reason_code is 'Code identifying the reason for the lucidity adjustment.';
    end if;
end $$;
comment on column professions.id is 'Primary key: bigint generated always as identity.';
comment on column professions.name is 'Profession name (must be unique).';
comment on column professions.stat_requirements is 'JSON object defining minimum stat requirements for the profession.';
comment on column professions.mechanical_effects is 'JSON object defining mechanical bonuses/penalties for the profession.';

-- ============================================================================
-- Cleanup: Drop helper function
-- ============================================================================
drop function if exists convert_serial_to_identity(text, text, text);

-- ============================================================================
-- Migration complete
-- ============================================================================
-- This migration has:
-- 1. Converted all serial/SERIAL columns to bigint generated always as identity
-- 2. Converted INTEGER primary keys to bigint generated always as identity
-- 3. Converted unnecessary varchar(n) columns to text
-- 4. Added table and column comments for documentation
--
-- Next steps:
-- 1. Update schema files (db/schema/*.sql) to match these changes
-- 2. Test all database operations to ensure compatibility
-- 3. Update SQLAlchemy models if needed
-- 4. Run this migration on production after thorough testing
