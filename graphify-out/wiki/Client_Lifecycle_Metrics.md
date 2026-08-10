# Client Lifecycle Metrics

> 31 nodes

## Key Concepts

- **broadcast_message()** (13 connections) — `server/api/game.py`
- **GameStatusResponse** (9 connections) — `server/schemas/game/game.py`
- **BroadcastMessageResponse** (9 connections) — `server/schemas/game/game.py`
- **__init__.py** (7 connections) — `server/schemas/game/__init__.py`
- **game.py** (7 connections) — `server/schemas/game/game.py`
- **BroadcastStats** (6 connections) — `server/schemas/game/game.py`
- **TestBroadcastMessage** (6 connections) — `server/tests/unit/api/test_game.py`
- **BaseModel** (4 connections)
- **.test_broadcast_message_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **TestBroadcastMessageEdgeCases** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_no_recipients()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_error()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_missing_stats_key()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_empty_stats()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_logs_info()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_stats_structure()** (3 connections) — `server/tests/unit/api/test_game.py`
- **Broadcast a message to all connected players (admin only).      Requires superus** (1 connections) — `server/api/game.py`
- **Game domain schemas: status, broadcast, Mythos time.** (1 connections) — `server/schemas/game/__init__.py`
- **Game API response schemas for MythosMUD server.  This module provides Pydantic m** (1 connections) — `server/schemas/game/game.py`
- **Response model for game status endpoint.** (1 connections) — `server/schemas/game/game.py`
- **Statistics for a broadcast operation.** (1 connections) — `server/schemas/game/game.py`
- **Response model for broadcast message endpoint.** (1 connections) — `server/schemas/game/game.py`
- **Test broadcast_message endpoint.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message successfully broadcasts message.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test broadcast_message handles no recipients.** (1 connections) — `server/tests/unit/api/test_game.py`
- *... and 6 more nodes in this community*

## Relationships

- [Chat Panel Filtering](Chat_Panel_Filtering.md) (11 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (3 shared connections)
- [Archive Planning Code](Archive_Planning_Code.md) (2 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 97 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*