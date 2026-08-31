# IdleMovementHandler

> 104 nodes

## Key Concepts

- **IdleMovementHandler** (56 connections) — `server/npc/idle_movement.py`
- **test_idle_movement.py** (36 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **idle_movement.py** (18 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **patch** (8 connections)
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **idle_movement_handler()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_true()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_active()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_check()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_true_when_not_in_combat_and_probability_succeeds()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- *... and 79 more nodes in this community*

## Relationships

- [NPCMovementIntegration](NPCMovementIntegration.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (2 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [.__init__](__init__.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)
- [threading.py](threading.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 158 (84%)
- INFERRED: 30 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*