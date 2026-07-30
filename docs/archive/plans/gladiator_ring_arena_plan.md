# Gladiator Ring (Arena) Implementation Plan

**Integrated from:** implementation todos + arena implementation guidance. Use **existing subagents** where they fit (Codebase Explorer for Phase 1 pattern discovery; Test Suite Analyzer for Phase 4).

---

## Plan summary

- **Zone** `limbo/arena` and **subzone** `arena`.
- **121 rooms** in an 11x11 grid; **center room** (5,5) = tutorial exit and respawn.
- **Tutorial exit** and **death/lucidity respawn** → arena center.
- **NPCs** keep existing spawns and **also** get one spawn in a random arena room at startup.

---

## Frontmatter todos (for Cursor plan file)

If your plan file supports `todos:` in frontmatter, use:

```yaml
todos:
  - id: todo-zone-ddl
    content: Add zone limbo/arena to schema and DML (all three DBs)
    status: pending
  - id: todo-subzone-ddl
    content: Add subzone arena under zone limbo/arena in DML
    status: pending
  - id: todo-rooms-121
    content: Add 121 arena rooms (limbo_arena_arena_arena_r_c) to DML
    status: pending
  - id: todo-room-links
    content: Add room_links for 11x11 grid (north/south/east/west)
    status: pending
  - id: todo-migration
    content: Add Alembic migration for arena zone/subzone/rooms/links
    status: pending
  - id: todo-tutorial-exit
    content: Set tutorial bedroom instance_exit_room_id to arena center
    status: pending
  - id: todo-instance-manager-default
    content: Optionally set DEFAULT_EXIT_ROOM_ID to arena center
    status: pending
  - id: todo-respawn-constant
    content: Set DEFAULT_RESPAWN_ROOM to limbo_arena_arena_arena_5_5
    status: pending
  - id: todo-respawn-lucidity
    content: Confirm lucidity respawn uses DEFAULT_RESPAWN_ROOM
    status: pending
  - id: todo-arena-room-list
    content: Define 121 arena room IDs in npc_startup_service
    status: pending
  - id: todo-npc-second-pass
    content: Add NPC startup second pass to spawn one per def in random arena room
    status: pending
  - id: todo-npc-warmup
    content: Ensure room cache warmed before arena spawn pass
    status: pending
  - id: todo-tests-respawn
    content: Update tests for DEFAULT_RESPAWN_ROOM and tutorial exit
    status: pending
  - id: todo-tests-instance
    content: Update instance_manager/tutorial tests for exit room
    status: pending
  - id: todo-verify-cache
    content: Verify room cache load includes arena zone/rooms
    status: pending
  - id: todo-docs
    content: Update docs for respawn/tutorial exit if applicable
    status: pending
```

---

## 1. Schema and data: zone, subzone, rooms, links

**Room ID format** ([server/world_loader.py](server/world_loader.py)): `plane_zone_sub_zone_room_file` -> for zone `limbo/arena` and subzone `arena`, room IDs: `limbo_arena_arena_<room_stable_id>`.

- **Zone:** Add zone `stable_id = 'limbo/arena'`. If `chk_zones_zone_type` blocks it, add `arena` in a migration or use an existing type (e.g. `death`).
- **Subzone:** Add subzone `stable_id = 'arena'`, `zone_id` = new zone UUID.
- **Rooms:** 121 rooms with `stable_id` `limbo_arena_arena_arena_0_0` … `limbo_arena_arena_arena_10_10`. Center: **`limbo_arena_arena_arena_5_5`**.
- **Room links:** For each (r,c), add north/south/east/west to adjacent cells in [0,10]. Use room **UUIDs** in `from_room_id` / `to_room_id` ([room_links](data/db/mythos_dev_dml.sql)).

**Subagent:** Use **Codebase Explorer** when exploring DML/schema patterns (zones, subzones, rooms, room_links COPY format and procedures).

---

## 2. Tutorial exit and respawn

- Set tutorial bedroom `instance_exit_room_id` to `limbo_arena_arena_arena_5_5` in room attributes (all three DML files).
- Optionally set `InstanceManager.DEFAULT_EXIT_ROOM_ID` to same ([server/game/instance_manager.py](server/game/instance_manager.py)).
- In [server/services/player_respawn_service.py](server/services/player_respawn_service.py): `DEFAULT_RESPAWN_ROOM = "limbo_arena_arena_arena_5_5"`.
- Confirm lucidity/delirium respawn uses `DEFAULT_RESPAWN_ROOM`.

---

## 3. NPCs also spawn in arena

In [server/services/npc_startup_service.py](server/services/npc_startup_service.py):

- Define 121 arena room IDs (`limbo_arena_arena_arena_0_0` … `limbo_arena_arena_arena_10_10`).
- After existing required + optional spawn pass, add a second pass: one instance per definition in `random.choice(arena_room_ids)`.
- Ensure room cache is warmed before the arena spawn pass.

---

## 4. Tests and validation

- Update tests for `DEFAULT_RESPAWN_ROOM` and tutorial exit to expect `limbo_arena_arena_arena_5_5`.
- Update instance_manager/tutorial tests for exit room.
- Verify room cache load includes new zone/subzone/rooms.
- **Subagent:** Use **Test Suite Analyzer** for Phase 4 test coverage and test updates where helpful.

---

## Implementation references

- Room ID generation: [server/world_loader.py](server/world_loader.py) (`generate_room_id`)
- Zone/subzone/rooms schema: [db/mythos_dev_ddl.sql](db/mythos_dev_ddl.sql)
- Room procedures: [db/procedures/rooms.sql](db/procedures/rooms.sql)
- DML examples: [data/db/mythos_dev_dml.sql](data/db/mythos_dev_dml.sql)
- Detailed task list: [gladiator-ring-arena-implementation-todos.md](gladiator-ring-arena-implementation-todos.md)
