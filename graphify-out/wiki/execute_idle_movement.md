# .execute_idle_movement

> 14 nodes

## Key Concepts

- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **Core gating for idle movement (interval handled by scheduler).** (1 connections) — `server/npc/idle_movement.py`
- **Determine if an NPC should attempt idle movement. Checks multiple conditions: -…** (1 connections) — `server/npc/idle_movement.py`
- **Get exits from current room that stay within subzone boundaries. Args:…** (1 connections) — `server/npc/idle_movement.py`
- **Execute idle movement for an NPC. This method orchestrates the full idle…** (1 connections) — `server/npc/idle_movement.py`

## Relationships

- [IdleMovementHandler](IdleMovementHandler.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [.select_exit](select_exit.md) (2 shared connections)
- [.is_alive](is_alive.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*