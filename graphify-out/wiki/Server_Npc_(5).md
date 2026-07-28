# Server Npc (5)

> 129 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **NPCMovementIntegration** (24 connections) — `server/npc/movement_integration.py`
- **idle_movement.py** (17 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **._get_room_objects()** (4 connections) — `server/npc/movement_integration.py`
- **._update_room_occupancy()** (4 connections) — `server/npc/movement_integration.py`
- **._update_npc_instance_room_tracking()** (4 connections) — `server/npc/movement_integration.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- *... and 104 more nodes in this community*

## Relationships

- [Server Npc (6)](Server_Npc_%286%29.md) (9 shared connections)
- [Server Events](Server_Events.md) (8 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Models (6)](Server_Models_%286%29.md) (2 shared connections)
- [Server Utils (13)](Server_Utils_%2813%29.md) (2 shared connections)
- [Server Npc (3)](Server_Npc_%283%29.md) (2 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (1 shared connections)
- [Server Game (19)](Server_Game_%2819%29.md) (1 shared connections)
- [Server Npc](Server_Npc.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 412 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*