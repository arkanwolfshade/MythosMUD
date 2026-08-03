# idle npc movement

> 27 nodes

## Key Concepts

- **idle_movement.py** (17 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (4 connections) — `server/npc/npc_base.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **NPC Idle Movement Handler for MythosMUD.  This module provides idle movement f** (1 connections) — `server/npc/idle_movement.py`
- **Get exits from current room that stay within subzone boundaries.          Args** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weight for an exit based on distance from spawn.          Args:** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weights for all exits.          Args:             valid_exits: Dict** (1 connections) — `server/npc/idle_movement.py`
- **Select exit based on weighted probabilities.          Args:             exit_** (1 connections) — `server/npc/idle_movement.py`
- **Select an exit using weighted random selection favoring exits closer to spawn ro** (1 connections) — `server/npc/idle_movement.py`
- **Calculate approximate distance between two rooms.          This is a simplifie** (1 connections) — `server/npc/idle_movement.py`
- **Execute idle movement for an NPC.          This method orchestrates the full i** (1 connections) — `server/npc/idle_movement.py`
- *... and 2 more nodes in this community*

## Relationships

- [idle movement npc](idle_movement_npc.md) (17 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (1 shared connections)
- [models invite Any](models_invite_Any.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*