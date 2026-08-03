# error websocket handler

> 8 nodes

## Key Concepts

- **.get_lifecycle_statistics()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._compute_state_counts()** (3 connections) — `server/npc/lifecycle_manager.py`
- **._compute_type_counts()** (3 connections) — `server/npc/lifecycle_manager.py`
- **._compute_aggregate_counts()** (3 connections) — `server/npc/lifecycle_manager.py`
- **Get overall lifecycle statistics.          Returns:             Dictionary co** (1 connections) — `server/npc/lifecycle_manager.py`
- **Return counts of lifecycle records by current_state.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Return counts of lifecycle records by NPC type string.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Return (total_spawns, total_despawns, total_errors) across all lifecycle records** (1 connections) — `server/npc/lifecycle_manager.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*