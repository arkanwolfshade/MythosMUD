# .execute_idle_movement

> 21 nodes

## Key Concepts

- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **Get exits from current room that stay within subzone boundaries. Args:…** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weight for an exit based on distance from spawn. Args:…** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weights for all exits. Args: valid_exits: Dictionary of direction ->…** (1 connections) — `server/npc/idle_movement.py`
- **Select exit based on weighted probabilities. Args: exit_weights: List of…** (1 connections) — `server/npc/idle_movement.py`
- **Select an exit using weighted random selection favoring exits closer to spawn…** (1 connections) — `server/npc/idle_movement.py`
- **Calculate approximate distance between two rooms. This is a simplified distance…** (1 connections) — `server/npc/idle_movement.py`
- **Execute idle movement for an NPC. This method orchestrates the full idle…** (1 connections) — `server/npc/idle_movement.py`

## Relationships

- [IdleMovementHandler](IdleMovementHandler.md) (14 shared connections)
- [get_logger](get_logger.md) (5 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*