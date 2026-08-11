# Game Magic Spell

> 4 nodes

## Key Concepts

- **_max_connection_age_seconds()** (3 connections) — `server/realtime/memory_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/memory_monitor.py`
- **Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops.** (1 connections) — `server/realtime/memory_monitor.py`
- **Initialize the memory monitor with default settings.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*