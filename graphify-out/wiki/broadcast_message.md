# broadcast_message

> 18 nodes

## Key Concepts

- **broadcast_message()** (14 connections) — `server/api/game.py`
- **asyncio** (7 connections)
- **TestBroadcastMessage** (5 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_no_recipients()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_empty_stats()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_logs_info()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_missing_stats_key()** (4 connections) — `server/tests/unit/api/test_game.py`
- **post** (1 connections)
- **Broadcast a message to all connected players (admin only). Requires superuser…** (1 connections) — `server/api/game.py`
- **Test broadcast_message handles broadcast errors gracefully.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message handles missing successful_deliveries in stats.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message handles empty stats dictionary.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message logs info messages correctly.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message endpoint.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message successfully broadcasts message.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message handles no recipients.** (1 connections) — `server/tests/unit/api/test_game.py`

## Relationships

- [get_mythos_time](get_mythos_time.md) (3 shared connections)
- [test_game.py](test_game.py.md) (2 shared connections)
- [game/game.py](game-game.py.md) (2 shared connections)
- [.test_broadcast_message_broadcast_stats_structure](test_broadcast_message_broadcast_stats_structure.md) (2 shared connections)
- [User](User.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*