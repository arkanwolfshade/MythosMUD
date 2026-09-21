# patch

> 27 nodes

## Key Concepts

- **patch** (25 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestBuildNpcConnectArgs** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_already_correct_search_path_is_left_alone()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_known_env_database_sets_search_path_to_db_name()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_non_env_database_leaves_connect_args_unchanged()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_query_string_is_stripped_before_matching_db_name()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_env_fallback()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_initializes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_raises_on_invalid_url()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_existing_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_nullpool_for_test()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_reset_npc_database_resets_state()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestResetNPCDatabase** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() uses NullPool for test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test reset_npc_database() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test reset_npc_database() resets all global state.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_build_npc_connect_args: search_path normalization, extracted from…** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **A database name outside the known dev/unit/e2e set is not touched.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **mythos_unit's search_path is normalized to the database name itself.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **No normalization needed when search_path already matches the database name.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **The database name is taken before any '?' query string, e.g. ?sslmode=require.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() initializes engine when None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() returns existing engine if already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 2 more nodes in this community*

## Relationships

- [npc_database.py](npc_database.py.md) (14 shared connections)
- [asyncio](asyncio.md) (8 shared connections)
- [get_npc_database_path](get_npc_database_path.md) (4 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [.test_get_npc_engine_recreates_on_loop_change](test_get_npc_engine_recreates_on_loop_change.md) (1 shared connections)
- [.test_get_npc_session_maker](test_get_npc_session_maker.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 61 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*