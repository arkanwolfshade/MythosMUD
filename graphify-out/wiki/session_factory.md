# session_factory

> 25 nodes

## Key Concepts

- **session_factory()** (71 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_exploration_procedures.py** (15 connections) — `server/tests/integration/test_exploration_procedures.py`
- **async_sessionmaker** (11 connections)
- **AsyncSession** (11 connections)
- **asyncio** (9 connections)
- **UUID** (9 connections)
- **test_coordinate_validator_detects_conflict_via_stored_procedures()** (8 connections) — `server/tests/integration/test_exploration_procedures.py`
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
- **CoordinateValidator's func()/table_valued() calls reach the same procedures as…** (1 connections) — `server/tests/integration/test_exploration_procedures.py`
- **One zone/subzone with two rooms linked by a 'north' exit, both positioned on…** (1 connections) — `server/tests/integration/test_exploration_procedures.py`
- **Create a user and a player row. Yields the player_id.** (1 connections) — `server/tests/integration/test_exploration_procedures.py`
- **First call is newly-inserted (True); second, idempotent call is already-existed…** (1 connections) — `server/tests/integration/test_exploration_procedures.py`

## Relationships

- [test_room_write_procedures.py](test_room_write_procedures.py.md) (12 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (9 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (7 shared connections)
- [Player](Player.md) (5 shared connections)
- [test_calendar_procedures.py](test_calendar_procedures.py.md) (4 shared connections)
- [test_update_container_found_returns_the_id](test_update_container_found_returns_the_id.md) (4 shared connections)
- [subzone_with_override](subzone_with_override.md) (4 shared connections)
- [emote_row](emote_row.md) (3 shared connections)
- [zone_and_subzone](zone_and_subzone.md) (3 shared connections)
- [ExplorationService](ExplorationService.md) (3 shared connections)
- [test_db_connectivity_create_and_read_user](test_db_connectivity_create_and_read_user.md) (2 shared connections)
- [test_lucidity_round_trip.py](test_lucidity_round_trip.py.md) (2 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/integration/test_exploration_procedures.py`

## Audit Trail

- EXTRACTED: 69 (52%)
- INFERRED: 64 (48%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*