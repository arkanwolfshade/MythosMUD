# Quality Audit Report

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

- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Realtime Npc Event](Realtime_Npc_Event.md) (3 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (3 shared connections)
- [E 2 E Testing Approach](E_2_E_Testing_Approach.md) (3 shared connections)

## Source Files

- `server/api/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 32 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*