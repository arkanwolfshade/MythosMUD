# CombatBroadcastMixin

> 25 nodes · cohesion 0.24

## Key Concepts

- **session_factory()** (91 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_exploration_procedures.py** (15 connections) — `server/tests/integration/test_exploration_procedures.py`
- **async_sessionmaker** (11 connections)
- **AsyncSession** (11 connections)
- **asyncio** (9 connections)
- **UUID** (9 connections)
- **test_coordinate_validator_detects_conflict_via_stored_procedures()** (9 connections) — `server/tests/integration/test_exploration_procedures.py`
- **test_get_coordinate_conflicts_pairs_same_coordinate_rooms()** (7 connections) — `server/tests/integration/test_exploration_procedures.py`
- **test_mark_room_explored_new_then_existing()** (7 connections) — `server/tests/integration/test_exploration_procedures.py`
- **player_row()** (6 connections) — `server/tests/integration/test_exploration_procedures.py`
- **room_pair()** (6 connections) — `server/tests/integration/test_exploration_procedures.py`
- **test_count_coordinated_rooms_counts_positioned_rooms()** (6 connections) — `server/tests/integration/test_exploration_procedures.py`
- **test_get_explored_rooms_and_is_room_explored()** (6 connections) — `server/tests/integration/test_exploration_procedures.py`
- **test_get_room_exits_for_coordinate_generation_returns_the_link()** (6 connections) — `server/tests/integration/test_exploration_procedures.py`
- **test_get_room_id_by_stable_id_resolves_the_uuid()** (6 connections) — `server/tests/integration/test_exploration_procedures.py`
- **test_get_rooms_for_coordinate_generation_matches_pattern()** (6 connections) — `server/tests/integration/test_exploration_procedures.py`
- **test_get_room_id_by_stable_id_unknown_returns_null()** (5 connections) — `server/tests/integration/test_exploration_procedures.py`
- **fixture** (2 connections)
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Integration tests for db/procedures/exploration.sql (#633). Replaces raw SQL…** (1 connections) — `server/tests/integration/test_exploration_procedures.py`
- **A third room at the source room's exact coordinates conflicts with it -- one…** (1 connections) — `server/tests/integration/test_exploration_procedures.py`
- **One zone/subzone with two rooms linked by a 'north' exit, both positioned on…** (1 connections) — `server/tests/integration/test_exploration_procedures.py`
- **CoordinateValidator's func()/table_valued() calls reach the same procedures as…** (1 connections) — `server/tests/integration/test_exploration_procedures.py`
- **Create a user and a player row. Yields the player_id.** (1 connections) — `server/tests/integration/test_exploration_procedures.py`
- **First call is newly-inserted (True); second, idempotent call is already-existed…** (1 connections) — `server/tests/integration/test_exploration_procedures.py`

## Relationships

- [test_combat_persistence_handler_events.py](test_combat_persistence_handler_events.py.md) (12 shared connections)
- [EdgeDetailsPanel.tsx](EdgeDetailsPanel.tsx.md) (9 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (8 shared connections)
- [test_build_room_objects_without_environment_in_attributes](test_build_room_objects_without_environment_in_attributes.md) (7 shared connections)
- [overrides](overrides.md) (6 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (5 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Call_of_Cthulhu__The_Coloring_Book__2026-08-12.md) (4 shared connections)
- [UX Writing](UX_Writing.md) (4 shared connections)
- [command_helpers.py](command_helpers.py.md) (4 shared connections)
- [✅ Phase 2 Async Persistence Migration - COMPLETE](✅_Phase_2_Async_Persistence_Migration_-_COMPLETE.md) (3 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Dead_Light_and_Other_Dark_Turns__2026-08-12.md) (3 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_The_Grand_Grimoire_of_Cthulhu_Mythos_Magic__2026-08-12.md) (3 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/integration/test_exploration_procedures.py`

## Audit Trail

- EXTRACTED: 69 (45%)
- INFERRED: 85 (55%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*