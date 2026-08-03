# realtime player presence

> 10 nodes

## Key Concepts

- **TestGetMythosTime** (12 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_missing_stats_key()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_empty_stats()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_logs_info()** (3 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time endpoint.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time includes holiday data when available.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message handles missing successful_deliveries in stats.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message handles empty stats dictionary.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message logs info messages correctly.** (1 connections) — `server/tests/unit/api/test_game.py`

## Relationships

- [game rationale schemas](game_rationale_schemas.md) (6 shared connections)
- [error logging rationale](error_logging_rationale.md) (3 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)
- [holiday service services](holiday_service_services.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 29 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*