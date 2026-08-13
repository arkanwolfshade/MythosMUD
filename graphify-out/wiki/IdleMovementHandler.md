# IdleMovementHandler

> 34 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **Core gating for idle movement (interval handled by scheduler).** (1 connections) — `server/npc/idle_movement.py`
- **Determine if an NPC should attempt idle movement. Checks multiple conditions: -…** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via UUID lookup. Args: npc_id: NPC ID (string or…** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via string ID mapping. Args: npc_id: NPC ID as string…** (1 connections) — `server/npc/idle_movement.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_idle_movement.py](test_idle_movement.py.md) (22 shared connections)
- [EventBus](EventBus.md) (16 shared connections)
- [patch](patch.md) (8 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [idle_movement_handler](idle_movement_handler.md) (1 shared connections)
- [NPCMessageQueue](NPCMessageQueue.md) (1 shared connections)
- [.is_alive](is_alive.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 96 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*