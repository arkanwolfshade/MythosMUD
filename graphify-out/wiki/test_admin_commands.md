# test admin commands

> 46 nodes

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_initialize_npc_database()** (12 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (11 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (9 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEnsureNPCDatabaseDirectory** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_raises_on_none_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestResetNPCDatabase** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **reset_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_maker()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_reset_npc_database_resets_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_ensure_npc_database_directory_no_op_for_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_ensure_npc_database_directory_creates_directory()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Initialize database engine and session maker from configuration.          CRITIC** (2 connections) — `server/database.py`
- **Path** (2 connections)
- *... and 21 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (16 shared connections)
- [real time](real_time.md) (7 shared connections)
- [get item description from prototype()](get_item_description_from_prototype%28%29.md) (7 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (6 shared connections)
- [close db()](close_db%28%29.md) (5 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [test command parser](test_command_parser.md) (4 shared connections)
- [Test broadcast player mortally wounded](Test_broadcast_player_mortally_wounded.md) (4 shared connections)
- [Test resolve connection manager from](Test_resolve_connection_manager_from.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [NATS Anti Patterns Review 2026](NATS_Anti_Patterns_Review_2026.md) (3 shared connections)
- [Test load room cache successfully](Test_load_room_cache_successfully.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 195 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*