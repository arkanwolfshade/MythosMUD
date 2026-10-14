# log_room_broadcast_result

> 8 nodes

## Key Concepts

- **log_room_broadcast_result()** (12 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_player_death()** (5 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **test_log_room_broadcast_result_debug_on_success()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_log_room_broadcast_result_error_on_failed_deliveries()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Log a room broadcast's outcome -- error-level on any failed delivery, debug-…** (1 connections) — `server/services/combat_messaging/base.py`
- **Broadcast player death message to all players in the room.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **A room broadcast with failed_deliveries must log at error level, not just debug…** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **A clean room broadcast (no failures) stays at debug level.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`

## Relationships

- [.connection_manager](connection_manager.md) (4 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (3 shared connections)
- [CombatBroadcastMixin](CombatBroadcastMixin.md) (2 shared connections)
- [NpcDisposition](NpcDisposition.md) (1 shared connections)
- [MessageCategory](MessageCategory.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*