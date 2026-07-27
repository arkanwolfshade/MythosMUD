# Integration DB Fixtures

> 44 nodes · cohesion 0.07

## Key Concepts

- **session_factory()** (17 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (10 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_procedures_return_shape.py** (8 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_add_player_effect_generates_id()** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **async_sessionmaker** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **AsyncSession** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_lucidity_round_trip.py** (6 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **test_lucidity_adjustment_round_trip()** (6 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **db.py** (5 connections) — `server/tests/fixtures/integration/db.py`
- **_delete_mutable_integration_test_rows()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_get_npc_system_statistics_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **quest_seed_data()** (5 connections) — `server/tests/integration/test_quest_flow.py`
- **FixtureRequest** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_db_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **AsyncSession** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **AsyncEngine** (2 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 19 more nodes in this community*

## Relationships

- [[NPC Admin API]] (10 shared connections)
- [[API Test Fixtures]] (8 shared connections)
- [[Player Domain Model]] (7 shared connections)
- [[SQLAlchemy Model Base]] (4 shared connections)
- [[Quest Flow Integration]] (3 shared connections)
- [[Lucidity State Models]] (2 shared connections)
- [[NPC Database Sessions]] (1 shared connections)
- [[Lucidity Database Models]] (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 135 (83%)
- INFERRED: 27 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
