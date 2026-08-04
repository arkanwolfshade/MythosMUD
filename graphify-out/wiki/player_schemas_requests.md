# player schemas requests

> 6 nodes

## Key Concepts

- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **Calculate weight for an exit based on distance from spawn.          Args:** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weights for all exits.          Args:             valid_exits: Dict** (1 connections) — `server/npc/idle_movement.py`
- **Calculate approximate distance between two rooms.          This is a simplifie** (1 connections) — `server/npc/idle_movement.py`

## Relationships

- [idle movement npc](idle_movement_npc.md) (3 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*