# E 2 E Scenarios Scenario

> 17 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **test_should_idle_move_not_active()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_false()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_rooms()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Handler for NPC idle movement logic.      This class manages the decision-maki** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via UUID lookup.          Args:             npc_id:** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via string ID mapping.          Args:             n** (1 connections) — `server/npc/idle_movement.py`
- **Test should_idle_move() returns False when NPC is not active.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Movement is skipped when random.random() > idle_movement_probability.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Gating skips idle movement when combat service lists this NPC.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() returns False when NPC is not in combat.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _calculate_distance_to_room() with different rooms.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`

## Relationships

- [NPC Movement Integration](NPC_Movement_Integration.md) (15 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (10 shared connections)
- [Dual Connection Monitoring Guide](Dual_Connection_Monitoring_Guide.md) (8 shared connections)
- [Cursor Skills Arrange](Cursor_Skills_Arrange.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [test_perform_recovery_action_naive_datetime_cooldown](test_perform_recovery_action_naive_datetime_cooldown.md) (1 shared connections)
- [test_get_action_cooldown_success](test_get_action_cooldown_success.md) (1 shared connections)
- [Services Exploration Service](Services_Exploration_Service.md) (1 shared connections)
- [test_perform_recovery_action_with_location](test_perform_recovery_action_with_location.md) (1 shared connections)
- [Investigations Sessions Movement](Investigations_Sessions_Movement.md) (1 shared connections)
- [Manual Dependency Analysis](Manual_Dependency_Analysis.md) (1 shared connections)
- [test_perform_recovery_action_all_actions](test_perform_recovery_action_all_actions.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 86 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*