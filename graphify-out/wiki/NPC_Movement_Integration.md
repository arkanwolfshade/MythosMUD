# NPC Movement Integration

> 108 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **idle_movement.py** (17 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **.is_active()** (5 connections) — `server/models/game.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (4 connections) — `server/npc/npc_base.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **idle_movement_handler()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 83 more nodes in this community*

## Relationships

- [Realtime Service Bundle](Realtime_Service_Bundle.md) (12 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (3 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 340 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*