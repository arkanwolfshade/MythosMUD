# config models player

> 19 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **test_should_idle_move_disabled()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_true()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_no_attribute()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_empty_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Handler for NPC idle movement logic.      This class manages the decision-maki** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via UUID lookup.          Args:             npc_id:** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via string ID mapping.          Args:             n** (1 connections) — `server/npc/idle_movement.py`
- **Check if an NPC is currently in combat.          Args:             npc_instan** (1 connections) — `server/npc/idle_movement.py`
- **Test should_idle_move() returns False when idle movement is disabled.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() returns False when NPC is not alive.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() when NPC is in combat.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() handles missing in_combat attribute.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test get_valid_exits() with room having no exits.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`

## Relationships

- [idle movement npc](idle_movement_npc.md) (18 shared connections)
- [idle npc movement](idle_npc_movement.md) (10 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (10 shared connections)
- [game room service](game_room_service.md) (4 shared connections)
- [commands exploration rationale](commands_exploration_rationale.md) (3 shared connections)
- [room game service](room_game_service.md) (3 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (2 shared connections)
- [event bus events](event_bus_events.md) (1 shared connections)
- [events event bus](events_event_bus.md) (1 shared connections)
- [npc idle movement](npc_idle_movement.md) (1 shared connections)
- [realtime player event](realtime_player_event.md) (1 shared connections)
- [conftest BoundLogger rationale](conftest_BoundLogger_rationale.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 91 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*