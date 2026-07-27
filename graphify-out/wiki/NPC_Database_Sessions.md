# NPC Database Sessions

> 10 nodes · cohesion 0.03

## Key Concepts

- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **AsyncEngine** (2 connections) — `server/npc_database.py`
- **Path** (2 connections) — `server/npc_database.py`
- **Get the NPC database engine, initializing if necessary.      Returns:         As** (1 connections) — `server/npc_database.py`
- **Reset NPC database state for testing.      This function resets all global NPC d** (1 connections) — `server/npc_database.py`
- **Get the NPC database file path.      DEPRECATED: PostgreSQL does not use file pa** (1 connections) — `server/npc_database.py`
- **Ensure NPC database directory exists.      DEPRECATED: PostgreSQL does not use f** (1 connections) — `server/npc_database.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (6 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (2 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)

## Source Files

- `server/npc_database.py`

## Audit Trail

- EXTRACTED: 40 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*