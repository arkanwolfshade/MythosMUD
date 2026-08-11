# NPC Movement Integration

> 24 nodes

## Key Concepts

- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_true()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_no_attribute()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_filters_exits_outside_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_all_exits_invalid_subzone_returns_empty()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_single_exit()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_exit_selected()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_current_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Unit tests for idle movement.  Tests the IdleMovementHandler class.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Create a mock event bus.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() returns False when NPC is not alive.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Movement runs when random.random() <= idle_movement_probability (exclusive upper** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() when NPC is in combat.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() handles missing in_combat attribute.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Subzone boundary validation drops exits that would leave the NPC subzone.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **When every target fails boundary validation, valid exits dict is empty.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test select_exit() with single exit.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test execute_idle_movement() when no exit is selected.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test execute_idle_movement() when NPC has no current room.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`

## Relationships

- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (16 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [test_perform_recovery_action_naive_datetime_cooldown](test_perform_recovery_action_naive_datetime_cooldown.md) (1 shared connections)
- [test_get_action_cooldown_success](test_get_action_cooldown_success.md) (1 shared connections)
- [Services Exploration Service](Services_Exploration_Service.md) (1 shared connections)
- [test_perform_recovery_action_with_location](test_perform_recovery_action_with_location.md) (1 shared connections)
- [Investigations Sessions Movement](Investigations_Sessions_Movement.md) (1 shared connections)
- [Manual Dependency Analysis](Manual_Dependency_Analysis.md) (1 shared connections)
- [test_perform_recovery_action_all_actions](test_perform_recovery_action_all_actions.md) (1 shared connections)
- [test_perform_recovery_action_invalid_string_player_id](test_perform_recovery_action_invalid_string_player_id.md) (1 shared connections)
- [test_get_action_cooldown_string_player_id](test_get_action_cooldown_string_player_id.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*