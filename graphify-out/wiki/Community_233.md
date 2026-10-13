# Community 233

> 67 nodes

## Key Concepts

- **send_game_event()** (33 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (25 connections) — `server/realtime/connection_manager_api.py`
- **test_connection_manager_api.py** (14 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **resolve_lazy_attr()** (12 connections) — `server/realtime/connection_manager_lazy.py`
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **remove_online_player()** (9 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (9 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (9 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_lazy.py** (9 connections) — `server/realtime/connection_manager_lazy.py`
- **asyncio** (8 connections)
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (7 connections)
- **connection_manager_utils.py** (7 connections) — `server/realtime/connection_manager_utils.py`
- **test_connection_manager_lazy.py** (6 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **test_missing_manager_is_logged_not_raised()** (5 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **ConnectionManagerUnavailable** (4 connections) — `server/realtime/connection_manager_api.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **test_resolve_lazy_attr_returns_api_function()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **test_broadcast_game_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_is_a_noop_without_a_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- *... and 42 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (12 shared connections)
- [Community 893](Community_893.md) (5 shared connections)
- [Community 41](Community_41.md) (3 shared connections)
- [WebSocket Message Types](WebSocket_Message_Types.md) (3 shared connections)
- [API Response Models](API_Response_Models.md) (2 shared connections)
- [Community 470](Community_470.md) (2 shared connections)
- [Community 254](Community_254.md) (2 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (2 shared connections)
- [Community 206](Community_206.md) (2 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (2 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (2 shared connections)
- [Community 452](Community_452.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/realtime/connection_manager_utils.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`
- `server/tests/unit/realtime/test_connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 154 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*