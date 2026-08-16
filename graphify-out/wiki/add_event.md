# .add_event

> 7 nodes

## Key Concepts

- **.add_event()** (5 connections) — `server/npc/lifecycle_types.py`
- **.change_state()** (4 connections) — `server/npc/lifecycle_types.py`
- **.get_statistics()** (3 connections) — `server/npc/lifecycle_types.py`
- **Any** (2 connections)
- **Return a snapshot of this record's stats (counts, times, state, age). Returns:…** (1 connections) — `server/npc/lifecycle_types.py`
- **Append a lifecycle event and update counters (spawn_count, despawn_count,…** (1 connections) — `server/npc/lifecycle_types.py`
- **Set the record's lifecycle state and record active-time delta; logs…** (1 connections) — `server/npc/lifecycle_types.py`

## Relationships

- [NPCDied](NPCDied.md) (3 shared connections)
- [despawn_npc_impl](despawn_npc_impl.md) (1 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_types.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*