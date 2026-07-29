# broadcast message()

> 10 nodes

## Key Concepts

- **broadcast_message()** (13 connections) — `server/api/game.py`
- **TestBroadcastMessage** (6 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_no_recipients()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_error()** (3 connections) — `server/tests/unit/api/test_game.py`
- **Broadcast a message to all connected players (admin only).      Requires superus** (1 connections) — `server/api/game.py`
- **Test broadcast_message endpoint.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message successfully broadcasts message.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message handles no recipients.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message handles broadcast errors gracefully.** (1 connections) — `server/tests/unit/api/test_game.py`

## Relationships

- [game](game.md) (3 shared connections)
- [test game](test_game.md) (3 shared connections)
- [Test get mythos time endpoint.](Test_get_mythos_time_endpoint.md) (3 shared connections)
- [APIRouter](APIRouter.md) (2 shared connections)
- [BaseUserManager](BaseUserManager.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 32 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*