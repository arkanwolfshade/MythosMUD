# DDL Application Status

## Database Verification Results

### mythos_dev (local development)

**Status**: ⚠️ PARTIAL - Missing runtime tables

**Existing Tables (21)**:

✅ Static tables: calendar_holidays, calendar_npc_schedules, emotes, emote_aliases, zones, subzones, rooms, room_links,
  aliases

✅ NPC tables: npc_definitions, npc_relationships, npc_spawn_rules

✅ Identity tables: professions, muting_rules, id_map_users, id_map_players

✅ Runtime tables: users, players, invites

- ✅ Item tables: item_prototypes, item_instances, item_component_states
- ❌ **MISSING**: player_inventories, player_sanity, sanity_adjustment_log, sanity_exposure_state, sanity_cooldowns

**Note**: Existing `players` table has different schema (UUID `id` primary key instead of VARCHAR `player_id`). This
needs migration.

### mythos_unit (unit tests)

**Status**: ✅ COMPLETE

**Existing Tables (27)**:

✅ All static tables

✅ All NPC tables

✅ All identity tables

✅ All runtime tables including: player_inventories, player_sanity, sanity_adjustment_log, sanity_exposure_state,

  sanity_cooldowns

✅ All item tables

### mythos_e2e (E2E tests)

**Status**: ⚠️ PARTIAL - Missing runtime tables

**Existing Tables (21)**:

✅ Static tables: calendar_holidays, calendar_npc_schedules, emotes, emote_aliases, zones, subzones, rooms, room_links,
  aliases

✅ NPC tables: npc_definitions, npc_relationships, npc_spawn_rules

✅ Identity tables: professions, muting_rules, id_map_users, id_map_players

✅ Item tables: item_prototypes, item_instances, item_component_states

✅ Runtime tables: users, invites

❌ **MISSING**: players, player_inventories, player_sanity, sanity_adjustment_log, sanity_exposure_state,

  sanity_cooldowns

## Required Actions

1. **mythos_dev**: Apply missing runtime tables (player_inventories, player_sanity, sanity_* tables)
2. **mythos_e2e**: Apply missing runtime tables (players, player_inventories, player_sanity, sanity_* tables)
3. **mythos_unit**: ✅ No action needed - all tables exist

## Schema Files to Apply

Apply in order:

1. `db/schema/01_world_and_calendar.sql` - ✅ Applied to all
2. `db/schema/02_items_and_npcs.sql` - ✅ Applied to all
3. `db/schema/03_identity_and_moderation.sql` - ✅ Applied to all
4. `db/schema/04_runtime_tables.sql` - ⚠️ Partially applied (missing some tables)
