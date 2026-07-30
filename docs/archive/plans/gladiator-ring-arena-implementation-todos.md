# Gladiator Ring (Arena) — Implementation Todos

This document provides the detailed todo list for the arena implementation plan. Use it to
track progress. Use existing subagents where they fit (e.g. Codebase Explorer for Phase 1
pattern discovery; Test Suite Analyzer for Phase 4).

**Plan reference:** Gladiator ring arena (zone `limbo/arena`, subzone `arena`, 11x11 grid,
center room = tutorial exit and respawn, NPCs also spawn in random arena room).

**Status:** Implementation complete (Phases 1–4). All tests passing.

**Arena DML process:** Arena lives in `mythos_dev_dml.sql`. For mythos_unit and mythos_e2e, arena is applied via
migration SQL: `data/db/migrations/20260227_add_arena_zone_unit.sql` and `20260227_add_arena_zone_e2e.sql`, generated
by `python scripts/gen_arena_migration_sql.py` and applied by `scripts/apply_arena_migration.ps1`. The legacy
`arena_rooms.txt` / `arena_links.txt` files have been removed.

---

## Todos (detailed)

### Phase 1: Schema and world data (Codebase Explorer for DML/schema pattern discovery) — DONE

- **todo-zone-ddl**: Add zone `limbo/arena` to schema/DML. If `chk_zones_zone_type` does not
  allow a new type, add `arena` in a small Alembic migration or use existing type (e.g.
  `death`). Insert zone row with `stable_id = 'limbo/arena'`, name, zone_type, environment,
  description, weather_patterns, special_rules in mythos_dev_dml, mythos_unit_dml,
  mythos_e2e_dml.
- **todo-subzone-ddl**: Add subzone `arena` with `stable_id = 'arena'`, `zone_id` = new zone
  UUID, name, environment, description, special_rules in all three DML files.
- **todo-rooms-121**: Generate 121 arena rooms: `stable_id` values
  `limbo_arena_arena_arena_0_0` … `limbo_arena_arena_arena_10_10`. Each row: id (UUID),
  subzone_id (arena subzone UUID), stable_id, name, description, attributes (e.g.
  `{"environment": "arena"}`). Use deterministic UUIDs for reproducibility. Add to
  mythos_dev_dml, mythos_unit_dml, mythos_e2e_dml (or one migration + DML sync).
- **todo-room-links**: Generate room_links for 11x11 grid: for each (r,c), link to
  (r-1,c)=north, (r+1,c)=south, (r,c+1)=east, (r,c-1)=west when in [0,10]. Use room UUIDs
  from todo-rooms-121. Add to all three DML files.
- **todo-migration**: Add Alembic migration (or equivalent) that creates zone, subzone, 121
  rooms, and room_links for mythos_dev (and document sync to unit/e2e if DML is
  generated from DB).

### Phase 2: Tutorial exit and respawn (main agent)

- **todo-tutorial-exit**: Set tutorial bedroom `instance_exit_room_id` to
  `limbo_arena_arena_arena_5_5` in room attributes in mythos*dev_dml, mythos_unit_dml,
  mythos_e2e_dml (tutorial bedroom row in COPY mythos*\*\_dml.rooms).
- **todo-instance-manager-default**: Optionally set
  `InstanceManager.DEFAULT_EXIT_ROOM_ID` to `limbo_arena_arena_arena_5_5` in
  `server/game/instance_manager.py`.
- **todo-respawn-constant**: In `server/services/player_respawn_service.py`, set
  `DEFAULT_RESPAWN_ROOM = "limbo_arena_arena_arena_5_5"`.
- **todo-respawn-lucidity**: Confirm lucidity/delirium respawn paths in
  `player_respawn_service.py` use `DEFAULT_RESPAWN_ROOM` (no extra change if they
  already do).

### Phase 3: NPC startup — also spawn in arena (main agent) — DONE

- **todo-arena-room-list**: Define list of 121 arena room IDs
  (`limbo_arena_arena_arena_0_0` … `limbo_arena_arena_arena_10_10`) in
  `server/services/npc_startup_service.py` (constant or helper).
- **todo-npc-second-pass**: After existing required + optional spawn pass, add a second
  pass: for each definition that was spawned (or all definitions with valid primary
  spawn), call spawn once with `room_id = random.choice(arena_room_ids)`. Use
  `spawn_npc_instance`; confirm population/definition caps allow a second instance
  per definition or adjust as needed.
- **todo-npc-warmup**: Ensure room cache is warmed before arena spawn pass (reuse
  existing warmup used in `_determine_spawn_room`).

### Phase 4: Tests and validation (main agent / Test Suite Analyzer) — DONE

- **todo-tests-respawn**: Update any tests that assert `DEFAULT_RESPAWN_ROOM` or
  tutorial exit room to expect `limbo_arena_arena_arena_5_5` where appropriate.
- **todo-tests-instance**: Update instance_manager or tutorial tests that assert
  exit room ID.
- **todo-verify-cache**: Manually or in integration test verify room cache load
  includes new zone/subzone/rooms (get_rooms_with_exits). **Done:**
  `test_get_rooms_with_exits_includes_arena_zone_rooms` in
  `server/tests/integration/test_procedures_return_shape.py` (requires test DB seeded from
  mythos_unit_dml.sql).
- **todo-docs**: Update any player-facing or dev docs that reference default respawn
  or tutorial exit (if applicable). **Done:** QUICK_START_E2E_TESTS.md, SUBSYSTEM_STATUS_EFFECTS_DESIGN.md.

---

## Subagent usage

| Phase / Task block                               | Recommended executor                                |
| ------------------------------------------------ | --------------------------------------------------- |
| Phase 1 (zone, subzone, rooms, links, migration) | Codebase Explorer (pattern discovery) or main agent |
| Phase 2 (tutorial exit, respawn constant)        | Main agent                                          |
| Phase 3 (NPC arena spawn pass)                   | Main agent                                          |
| Phase 4 (tests, docs)                            | Main agent or Test Suite Analyzer                   |

---

## Plan frontmatter todos (for Cursor plan file)

Copy the following into the plan's frontmatter as `todos:` (replace existing `todos: []`):

```yaml
todos:
  - id: todo-zone-ddl
    content: Add zone limbo/arena to schema and DML (all three DBs)
  - id: todo-subzone-ddl
    content: Add subzone arena under zone limbo/arena in DML
  - id: todo-rooms-121
    content: Add 121 arena rooms (limbo_arena_arena_arena_r_c) to DML
  - id: todo-room-links
    content: Add room_links for 11x11 grid (north/south/east/west)
  - id: todo-migration
    content: Add Alembic migration for arena zone/subzone/rooms/links
  - id: todo-tutorial-exit
    content: Set tutorial bedroom instance_exit_room_id to arena center
  - id: todo-instance-manager-default
    content: Optionally set DEFAULT_EXIT_ROOM_ID to arena center
  - id: todo-respawn-constant
    content: Set DEFAULT_RESPAWN_ROOM to limbo_arena_arena_arena_5_5
  - id: todo-respawn-lucidity
    content: Confirm lucidity respawn uses DEFAULT_RESPAWN_ROOM
  - id: todo-arena-room-list
    content: Define 121 arena room IDs in npc_startup_service
  - id: todo-npc-second-pass
    content: Add NPC startup second pass to spawn one per def in random arena room
  - id: todo-npc-warmup
    content: Ensure room cache warmed before arena spawn pass
  - id: todo-tests-respawn
    content: Update tests for DEFAULT_RESPAWN_ROOM and tutorial exit
  - id: todo-tests-instance
    content: Update instance_manager/tutorial tests for exit room
  - id: todo-verify-cache
    content: Verify room cache load includes arena zone/rooms
  - id: todo-docs
    content: Update docs for respawn/tutorial exit if applicable
```
