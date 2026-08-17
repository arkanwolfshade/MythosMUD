# IdleMovementHandler

> 74 nodes

## Key Concepts

- **IdleMovementHandler** (56 connections) — `server/npc/idle_movement.py`
- **test_idle_movement.py** (36 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **patch** (8 connections)
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
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
- **test_calculate_distance_to_room_different_rooms()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_same_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_same_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_current_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_exit_selected()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_valid_exits()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_all_exits_invalid_subzone_returns_empty()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 49 more nodes in this community*

## Relationships

- [.execute_idle_movement](execute_idle_movement.md) (14 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [idle_movement_handler](idle_movement_handler.md) (4 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (1 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (1 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 111 (77%)
- INFERRED: 33 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*