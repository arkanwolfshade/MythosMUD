# IdleMovementHandler

> 84 nodes

## Key Concepts

- **IdleMovementHandler** (56 connections) — `server/npc/idle_movement.py`
- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **patch** (8 connections)
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **test_is_npc_in_combat_true()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_active()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_check()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_true_when_not_in_combat_and_probability_succeeds()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **test_calculate_distance_to_room_different_rooms()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 59 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [.select_exit](select_exit.md) (7 shared connections)
- [idle_movement_handler](idle_movement_handler.md) (4 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (2 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (2 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 129 (81%)
- INFERRED: 30 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*