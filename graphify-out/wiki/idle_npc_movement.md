# idle npc movement

> 34 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **Handler for NPC idle movement logic.      This class manages the decision-maki** (1 connections) — `server/npc/idle_movement.py`
- **Core gating for idle movement (interval handled by scheduler).** (1 connections) — `server/npc/idle_movement.py`
- **Determine if an NPC should attempt idle movement.          Checks multiple con** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via UUID lookup.          Args:             npc_id:** (1 connections) — `server/npc/idle_movement.py`
- *... and 9 more nodes in this community*

## Relationships

- [idle movement npc](idle_movement_npc.md) (23 shared connections)
- [NATS Messaging](NATS_Messaging.md) (11 shared connections)
- [npc idle movement](npc_idle_movement.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [combat services initialization](combat_services_initialization.md) (2 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (1 shared connections)
- [combat service services](combat_service_services.md) (1 shared connections)
- [services combat sync](services_combat_sync.md) (1 shared connections)
- [realtime maintenance rationale](realtime_maintenance_rationale.md) (1 shared connections)
- [models profession repr](models_profession_repr.md) (1 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 149 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*