# idle movement npc

> 30 nodes

## Key Concepts

- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **idle_movement_handler()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init_no_persistence()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_check()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_false()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_keeps_all_exits_when_subzone_boundary_allows()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_empty_dict()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_multiple_exits()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_same_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_current_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Unit tests for idle movement.  Tests the IdleMovementHandler class.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Create a mock event bus.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Create an IdleMovementHandler instance.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test IdleMovementHandler initialization fails without persistence.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() respects movement probability (random > threshold fails)** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Movement runs when random.random() <= idle_movement_probability (exclusive upper** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Movement is skipped when random.random() > idle_movement_probability.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Gating skips idle movement when combat service lists this NPC.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() returns False when NPC is not in combat.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 5 more nodes in this community*

## Relationships

- [config models player](config_models_player.md) (18 shared connections)
- [game room service](game_room_service.md) (4 shared connections)
- [room game service](room_game_service.md) (3 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [event bus events](event_bus_events.md) (1 shared connections)
- [events event bus](events_event_bus.md) (1 shared connections)
- [npc idle movement](npc_idle_movement.md) (1 shared connections)
- [realtime player event](realtime_player_event.md) (1 shared connections)
- [conftest BoundLogger rationale](conftest_BoundLogger_rationale.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 90 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*