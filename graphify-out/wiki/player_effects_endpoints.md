# player effects endpoints

> 33 nodes

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
- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestResetNPCDatabase** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **reset_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_maker()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_reset_npc_database_resets_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Path** (2 connections)
- **Dependency to get NPC database session.      Yields:         AsyncSession: Datab** (2 connections) — `server/npc_database.py`
- **NPC Database configuration for MythosMUD.  This module provides database connect** (1 connections) — `server/npc_database.py`
- **Initialize NPC database engine and session maker from configuration.      CRITIC** (1 connections) — `server/npc_database.py`
- **Get the NPC async session maker, initializing if necessary.      Returns:** (1 connections) — `server/npc_database.py`
- **Initialize NPC database connection and verify configuration.      NOTE: DDL (tab** (1 connections) — `server/npc_database.py`
- **Close NPC database connections.** (1 connections) — `server/npc_database.py`
- **Reset NPC database state for testing.      This function resets all global NPC d** (1 connections) — `server/npc_database.py`
- *... and 8 more nodes in this community*

## Relationships

- [command inventory models](command_inventory_models.md) (10 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [schemas players profession](schemas_players_profession.md) (7 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (4 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [shutdown commands admin](shutdown_commands_admin.md) (4 shared connections)
- [commands command validation](commands_command_validation.md) (4 shared connections)
- [admin auth service](admin_auth_service.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 167 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*