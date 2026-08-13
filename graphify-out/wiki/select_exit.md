# .select_exit

> 11 nodes

## Key Concepts

- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **Calculate weight for an exit based on distance from spawn. Args:…** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weights for all exits. Args: valid_exits: Dictionary of direction ->…** (1 connections) — `server/npc/idle_movement.py`
- **Select exit based on weighted probabilities. Args: exit_weights: List of…** (1 connections) — `server/npc/idle_movement.py`
- **Select an exit using weighted random selection favoring exits closer to spawn…** (1 connections) — `server/npc/idle_movement.py`
- **Calculate approximate distance between two rooms. This is a simplified distance…** (1 connections) — `server/npc/idle_movement.py`

## Relationships

- [IdleMovementHandler](IdleMovementHandler.md) (5 shared connections)
- [.execute_idle_movement](execute_idle_movement.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*