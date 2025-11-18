-- MythosMUD Schema: World, Calendar, and Emotes
-- Apply to each database as owner role (mythos_owner_*).
-- UUIDs: Static datasets will use deterministic v5 UUIDs generated in data load scripts.
-- For runtime-created rows (if any), defaults can use gen_random_uuid().

SET client_min_messages = WARNING;
SET search_path = public;

-- Enumerations (expand as needed)
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'season_enum') THEN
        CREATE TYPE season_enum AS ENUM ('winter', 'spring', 'summer', 'autumn');
    END IF;
END$$;

-- Calendar: Holidays
CREATE TABLE IF NOT EXISTS calendar_holidays (
    id              uuid PRIMARY KEY,
    stable_id       text NOT NULL UNIQUE,      -- e.g., 'mary_mother_of_god'
    name            text NOT NULL,
    tradition       text NOT NULL,
    month           smallint NOT NULL CHECK (month BETWEEN 1 AND 12),
    day             smallint NOT NULL CHECK (day BETWEEN 1 AND 31),
    duration_hours  smallint NOT NULL CHECK (duration_hours BETWEEN 1 AND 168),
    season          season_enum NOT NULL,
    bonus_tags      text[] NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_calendar_holidays_tradition ON calendar_holidays(tradition);
CREATE INDEX IF NOT EXISTS idx_calendar_holidays_month_day ON calendar_holidays(month, day);

-- Calendar: NPC Schedules
CREATE TABLE IF NOT EXISTS calendar_npc_schedules (
    id              uuid PRIMARY KEY,
    stable_id       text NOT NULL UNIQUE,      -- e.g., 'arkham_shop_day_shift'
    name            text NOT NULL,
    category        text NOT NULL,            -- 'npc' (free text kept from JSON)
    start_hour      smallint NOT NULL CHECK (start_hour BETWEEN 0 AND 24),
    end_hour        smallint NOT NULL CHECK (end_hour BETWEEN 0 AND 24),
    days            text[] NOT NULL,          -- e.g., ["Primus", ...]
    applies_to      text[] NOT NULL,          -- e.g., ["shopkeeper", "vendor"]
    effects         text[] NOT NULL,          -- e.g., ["shops_open", ...]
    notes           text
);
CREATE INDEX IF NOT EXISTS idx_calendar_npc_schedules_category ON calendar_npc_schedules(category);
CREATE INDEX IF NOT EXISTS idx_calendar_npc_schedules_hours ON calendar_npc_schedules(start_hour, end_hour);

-- Emotes (global)
CREATE TABLE IF NOT EXISTS emotes (
    id              uuid PRIMARY KEY,
    stable_id       text NOT NULL UNIQUE,      -- canonical emote key e.g., 'twibble'
    self_message    text NOT NULL,
    other_message   text NOT NULL
);
CREATE TABLE IF NOT EXISTS emote_aliases (
    emote_id        uuid NOT NULL REFERENCES emotes(id) ON DELETE CASCADE,
    alias           text NOT NULL,
    PRIMARY KEY (emote_id, alias)
);
CREATE INDEX IF NOT EXISTS idx_emote_alias_on_alias ON emote_aliases(alias);

-- World structure
CREATE TABLE IF NOT EXISTS zones (
    id              uuid PRIMARY KEY,
    stable_id       text NOT NULL UNIQUE,  -- e.g., 'earth/arkhamcity'
    name            text NOT NULL
);

CREATE TABLE IF NOT EXISTS subzones (
    id              uuid PRIMARY KEY,
    zone_id         uuid NOT NULL REFERENCES zones(id) ON DELETE CASCADE,
    stable_id       text NOT NULL,         -- e.g., 'downtown'
    name            text NOT NULL,
    UNIQUE(zone_id, stable_id)
);
CREATE INDEX IF NOT EXISTS idx_subzones_zone ON subzones(zone_id);

-- Zone configurations (zone and subzone level settings)
CREATE TABLE IF NOT EXISTS zone_configurations (
    id              uuid PRIMARY KEY,
    zone_id         uuid REFERENCES zones(id) ON DELETE CASCADE,
    subzone_id      uuid REFERENCES subzones(id) ON DELETE CASCADE,
    configuration_type text NOT NULL CHECK (configuration_type IN ('zone', 'subzone')),
    environment     text,
    description     text,
    weather_patterns jsonb DEFAULT '[]'::jsonb,
    special_rules   jsonb DEFAULT '{}'::jsonb,
    UNIQUE(zone_id, subzone_id, configuration_type)
);
CREATE INDEX IF NOT EXISTS idx_zone_configs_zone ON zone_configurations(zone_id);
CREATE INDEX IF NOT EXISTS idx_zone_configs_subzone ON zone_configurations(subzone_id);

CREATE TABLE IF NOT EXISTS rooms (
    id              uuid PRIMARY KEY,
    subzone_id      uuid NOT NULL REFERENCES subzones(id) ON DELETE CASCADE,
    stable_id       text NOT NULL,         -- file-derived id e.g., 'room_derby_st_001'
    name            text NOT NULL,
    description     text NOT NULL,
    attributes      jsonb NOT NULL DEFAULT '{}'::jsonb, -- arbitrary room metadata from JSON
    UNIQUE(subzone_id, stable_id)
);
CREATE INDEX IF NOT EXISTS idx_rooms_subzone ON rooms(subzone_id);

-- Directed links between rooms (exits)
CREATE TABLE IF NOT EXISTS room_links (
    id              uuid PRIMARY KEY,
    from_room_id    uuid NOT NULL REFERENCES rooms(id) ON DELETE CASCADE,
    to_room_id      uuid NOT NULL REFERENCES rooms(id) ON DELETE RESTRICT,
    direction       text NOT NULL,         -- e.g., 'north', 'southwest', etc.
    attributes      jsonb NOT NULL DEFAULT '{}'::jsonb,
    UNIQUE(from_room_id, direction)
);
CREATE INDEX IF NOT EXISTS idx_room_links_from ON room_links(from_room_id);
CREATE INDEX IF NOT EXISTS idx_room_links_to ON room_links(to_room_id);

-- Aliases: could apply to rooms, subzones, zones, or commands
CREATE TABLE IF NOT EXISTS aliases (
    id              uuid PRIMARY KEY,
    target_type     text NOT NULL,         -- 'emote' | 'room' | 'zone' | 'subzone' | 'command'
    target_id       uuid NOT NULL,         -- references table based on target_type (validated in app logic)
    alias           text NOT NULL,
    UNIQUE(target_type, target_id, alias)
);
CREATE INDEX IF NOT EXISTS idx_aliases_type_id ON aliases(target_type, target_id);
