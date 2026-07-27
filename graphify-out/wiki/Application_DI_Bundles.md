# Application DI Bundles

> 11 nodes · cohesion 0.02

## Key Concepts

- **init_npc_db()** (10 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **Any** (7 connections) — `server/container/bundles/realtime.py`
- **Any** (5 connections) — `server/events/distributed_event_bus.py`
- **Any** (3 connections) — `server/container/main.py`
- **Path** (2 connections) — `server/container/main.py`
- **Any** (1 connections) — `server/container/utils.py`
- **Path** (1 connections) — `server/container/utils.py`
- **Initialize NPC database connection and verify configuration.      NOTE: DDL (tab** (1 connections) — `server/npc_database.py`
- **Close NPC database connections.** (1 connections) — `server/npc_database.py`
- **Any** (1 connections) — `server/tests/fixtures/unit/__init__.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`
- `server/npc_database.py`
- `server/tests/fixtures/unit/__init__.py`

## Audit Trail

- EXTRACTED: 32 (78%)
- INFERRED: 9 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*