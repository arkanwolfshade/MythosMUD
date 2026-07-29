# Test get mythos time endpoint.

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

- [get mythos time()](get_mythos_time%28%29.md) (6 shared connections)
- [broadcast message()](broadcast_message%28%29.md) (3 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)
- [test game](test_game.md) (1 shared connections)
- [HolidayCollection](HolidayCollection.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 29 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*