# Time Service

> 19 nodes · cohesion 0.13

## Key Concepts

- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **._load_state()** (7 connections) — `server/time/time_service.py`
- **._persist_state()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **.advance_mythos()** (4 connections) — `server/time/time_service.py`
- **.get_last_freeze_state()** (3 connections) — `server/time/time_service.py`
- **.get_state_snapshot()** (3 connections) — `server/time/time_service.py`
- **Path** (1 connections) — `server/time/time_service.py`
- **Return the current persisted state snapshot.** (1 connections) — `server/time/time_service.py`
- **Move the chronicle forward by a number of Mythos hours.          This helper is** (1 connections) — `server/time/time_service.py`
- **Capture the current state so the chronicle can resume deterministically after do** (1 connections) — `server/time/time_service.py`
- **Return the most recent freeze snapshot, if any.** (1 connections) — `server/time/time_service.py`
- **Migrate old state file from previous system (1930 epoch, 9.6 ratio) to new syste** (1 connections) — `server/time/time_service.py`
- **Load the chronicle state from disk or initialize from config defaults.** (1 connections) — `server/time/time_service.py`
- **Persist the provided state atomically.** (1 connections) — `server/time/time_service.py`
- **Snapshot of the chronicle's reference timestamps.      The last frozen real time** (1 connections) — `server/time/time_service.py`
- **TimeConfig** (1 connections) — `server/time/time_service.py`

## Relationships

- [[Async Task Registry]] (8 shared connections)
- [[Mythos Calendar Time Service]] (5 shared connections)
- [[NPC Admin API]] (2 shared connections)

## Source Files

- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
