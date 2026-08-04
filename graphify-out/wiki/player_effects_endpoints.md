# player effects endpoints

> 32 nodes

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (12 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (9 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **TestCloseNpcDb** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **reset_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Initialize database engine and session maker from configuration.          CRITIC** (2 connections) — `server/database.py`
- **AsyncEngine** (2 connections)
- **Dependency to get NPC database session.      Yields:         AsyncSession: Datab** (2 connections) — `server/npc_database.py`
- **NPC Database configuration for MythosMUD.  This module provides database connect** (1 connections) — `server/npc_database.py`
- **Initialize NPC database engine and session maker from configuration.      CRITIC** (1 connections) — `server/npc_database.py`
- **Get the NPC database engine, initializing if necessary.      Returns:         As** (1 connections) — `server/npc_database.py`
- **Get the NPC async session maker, initializing if necessary.      Returns:** (1 connections) — `server/npc_database.py`
- **Initialize NPC database connection and verify configuration.      NOTE: DDL (tab** (1 connections) — `server/npc_database.py`
- **Close NPC database connections.** (1 connections) — `server/npc_database.py`
- *... and 7 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (10 shared connections)
- [nats services service](nats_services_service.md) (7 shared connections)
- [persistence protocols rationale](persistence_protocols_rationale.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [schemas players profession](schemas_players_profession.md) (6 shared connections)
- [game models enums](game_models_enums.md) (4 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [shutdown commands admin](shutdown_commands_admin.md) (4 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [tools generate invite](tools_generate_invite.md) (3 shared connections)
- [level game service](level_game_service.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 170 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*