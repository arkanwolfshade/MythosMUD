# Container Persistence Layer

> 43 nodes

## Key Concepts

- **__init__.py** (18 connections) — `server/tests/fixtures/integration/__init__.py`
- **session_factory()** (17 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **db_cleanup()** (10 connections) — `server/tests/fixtures/integration/__init__.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
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
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_db_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **_IntegrationState** (2 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (2 connections)
- **Build connect_args for asyncpg when POSTGRES_SEARCH_PATH is set.      Used so un** (1 connections) — `server/database_config_helpers.py`
- *... and 18 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (7 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (4 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (2 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (1 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (1 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_procedures_return_shape.py`

## Audit Trail

- EXTRACTED: 153 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*