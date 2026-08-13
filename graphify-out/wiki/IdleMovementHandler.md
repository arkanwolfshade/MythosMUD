# IdleMovementHandler

> 19 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **test_execute_idle_movement_no_exit_selected()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_filters_exits_outside_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init_no_persistence()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_multiple_exits()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_single_exit()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Check if NPC is in combat via UUID lookup. Args: npc_id: NPC ID (string or…** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via string ID mapping. Args: npc_id: NPC ID as string…** (1 connections) — `server/npc/idle_movement.py`
- **Check if an NPC is currently in combat. Args: npc_instance: The NPC instance to…** (1 connections) — `server/npc/idle_movement.py`
- **Handler for NPC idle movement logic. This class manages the decision-making and…** (1 connections) — `server/npc/idle_movement.py`
- **Subzone boundary validation drops exits that would leave the NPC subzone.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test select_exit() with single exit.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test select_exit() with multiple exits.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test execute_idle_movement() when no exit is selected.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test IdleMovementHandler initialization fails without persistence.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`

## Relationships

- [test_idle_movement.py](test_idle_movement.py.md) (19 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (10 shared connections)
- [patch](patch.md) (8 shared connections)
- [.execute_idle_movement](execute_idle_movement.md) (7 shared connections)
- [.select_exit](select_exit.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_idle_movement_handler_init](test_idle_movement_handler_init.md) (1 shared connections)
- [test_calculate_distance_to_room_same_subzone](test_calculate_distance_to_room_same_subzone.md) (1 shared connections)
- [test_select_exit_empty_dict](test_select_exit_empty_dict.md) (1 shared connections)
- [idle_movement_handler](idle_movement_handler.md) (1 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 70 (91%)
- INFERRED: 7 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*