# Community 43

> 134 nodes

## Key Concepts

- **test_player_presence_tracker.py** (59 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (54 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (31 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (22 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (22 connections)
- **.async_persistence()** (19 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (11 connections)
- **UUID** (10 connections)
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id_for_tutorial_reconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_warm_corruption_tier_cache()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **test_tutorial_reentry_gives_stranded_player_a_fresh_instance()** (9 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_tutorial_reentry_ignores_players_outside_templates()** (9 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **_build_player_info()** (8 connections) — `server/realtime/player_presence_tracker.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_send_grace_reconnect_catchup()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (7 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_GraceReconnectManager** (6 connections) — `server/realtime/player_presence_tracker.py`
- **RoomLookup** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_stranded_template_id()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_manager_with()** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 109 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (39 shared connections)
- [Community 221](Community_221.md) (8 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (7 shared connections)
- [Community 76](Community_76.md) (5 shared connections)
- [Community 139](Community_139.md) (5 shared connections)
- [Community 41](Community_41.md) (3 shared connections)
- [Community 429](Community_429.md) (3 shared connections)
- [Community 188](Community_188.md) (2 shared connections)
- [Community 273](Community_273.md) (2 shared connections)
- [Community 441](Community_441.md) (2 shared connections)
- [API Response Models](API_Response_Models.md) (1 shared connections)
- [Community 130](Community_130.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 321 (93%)
- INFERRED: 25 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*