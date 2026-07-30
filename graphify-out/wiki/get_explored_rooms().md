# .get explored rooms()

> 19 nodes

## Key Concepts

- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **Core gating for idle movement (interval handled by scheduler).** (1 connections) — `server/npc/idle_movement.py`
- **Determine if an NPC should attempt idle movement.          Checks multiple con** (1 connections) — `server/npc/idle_movement.py`
- **Get exits from current room that stay within subzone boundaries.          Args** (1 connections) — `server/npc/idle_movement.py`
- **Select exit based on weighted probabilities.          Args:             exit_** (1 connections) — `server/npc/idle_movement.py`
- **Select an exit using weighted random selection favoring exits closer to spawn ro** (1 connections) — `server/npc/idle_movement.py`
- **Execute idle movement for an NPC.          This method orchestrates the full i** (1 connections) — `server/npc/idle_movement.py`

## Relationships

- [cfg float()](cfg_float%28%29.md) (9 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [Player](Player.md) (1 shared connections)
- [.get active status effects()](get_active_status_effects%28%29.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*