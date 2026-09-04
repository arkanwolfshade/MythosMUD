# Test Player Event Handlers Respawn

> 109 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (53 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_respawn.py** (38 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **asyncio** (22 connections)
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **_async_persistence()** (10 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_logger_method()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **UUID** (7 connections)
- **._build_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._emit_respawn_room_posture()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_send_personal_message()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_delirium_respawn_error_handling()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_respawn_error_handling()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_respawn_no_get_stats()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_handle_player_delirium_respawned_success()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_handle_player_respawned_success()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **RespawnPlayerStatsPayload** (5 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **._build_fallback_respawn_player_payload()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 84 more nodes in this community*

## Relationships

- [Test Event Handler](Test_Event_Handler.md) (6 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (5 shared connections)
- [Player Event Handlers](Player_Event_Handlers.md) (2 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (2 shared connections)
- [Player Event Handlers Respawn Room](Player_Event_Handlers_Respawn_Room.md) (2 shared connections)
- [Player Event Handlers Respawn](Player_Event_Handlers_Respawn.md) (1 shared connections)
- [Posture Notify](Posture_Notify.md) (1 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 213 (89%)
- INFERRED: 27 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*