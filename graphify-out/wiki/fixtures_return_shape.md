# fixtures return shape

> 40 nodes

## Key Concepts

- **session_factory()** (17 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **db_cleanup()** (10 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_add_player_effect_generates_id()** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **_delete_mutable_integration_test_rows()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_get_rooms_with_exits_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **async_sessionmaker** (5 connections)
- **AsyncSession** (5 connections)
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_npc_system_statistics_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **quest_seed_data()** (5 connections) — `server/tests/integration/test_quest_flow.py`
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_db_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (2 connections)
- **AsyncEngine** (1 connections)
- **Extract database name from a PostgreSQL URL. Returns empty string on parse failu** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True only if the URL points to an allowed test-only database (mythos_unit** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 15 more nodes in this community*

## Relationships

- [world models rationale](world_models_rationale.md) (11 shared connections)
- [auth users rationale](auth_users_rationale.md) (5 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 128 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*