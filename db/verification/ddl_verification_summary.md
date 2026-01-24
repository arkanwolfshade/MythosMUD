# DDL Verification Summary

## Final Status

### mythos_dev (local development)

**Status**: ✅ COMPLETE (29 tables)

**All Required Tables Present**:

✅ Static tables (9): calendar_holidays, calendar_npc_schedules, emotes, emote_aliases, zones, subzones, rooms,
  room_links, aliases

✅ NPC tables (3): npc_definitions, npc_relationships, npc_spawn_rules

✅ Identity tables (4): professions, muting_rules, id_map_users, id_map_players

✅ Runtime tables (8): users, players, player_inventories, invites, player_sanity, sanity_adjustment_log,

  sanity_exposure_state, sanity_cooldowns

✅ Item tables (3): item_prototypes, item_instances, item_component_states

**Note**: `mythos_dev` has an older `players` table schema (UUID `id` primary key) that differs from the DDL
specification (VARCHAR `player_id`). The missing runtime tables have been created with foreign keys referencing the
existing `players.id` column.

### mythos_unit (unit tests)

**Status**: ✅ COMPLETE (27 tables)

**All Required Tables Present**:

✅ All static tables

✅ All NPC tables

✅ All identity tables

✅ All runtime tables (including player_inventories, player_sanity, sanity_* tables)

- ✅ All item tables

### mythos_e2e (E2E tests)

**Status**: ✅ COMPLETE (27 tables)

**All Required Tables Present**:

✅ Static tables (9)

✅ NPC tables (3)

✅ Identity tables (4)

✅ Runtime tables (8): users, players, player_inventories, invites, player_sanity, sanity_adjustment_log,

  sanity_exposure_state, sanity_cooldowns

✅ Item tables (3)

## Schema Files Applied

All schema files have been applied to all three databases:

1. ✅ `db/schema/01_world_and_calendar.sql` - Applied
2. ✅ `db/schema/02_items_and_npcs.sql` - Applied
3. ✅ `db/schema/03_identity_and_moderation.sql` - Applied
4. ✅ `db/schema/04_runtime_tables.sql` - Applied (with adaptations for mythos_dev's existing schema)

## Notes

**mythos_dev schema difference**: The existing `players` table uses UUID `id` as primary key instead of VARCHAR
  `player_id`. This is from the old SQLAlchemy-created schema. The runtime tables (player_sanity, sanity_*,
  player_inventories) have been created with foreign keys referencing `players.id` to match the existing structure.

**Migration consideration**: If `mythos_dev` needs to match the DDL specification exactly, a migration script would be
  needed to:

  1. Rename `players.id` to `players.player_id` and change type to VARCHAR(255)
  2. Update all foreign key references
  3. Migrate existing data
