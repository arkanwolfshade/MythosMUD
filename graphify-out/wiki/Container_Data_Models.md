# Container Data Models

> 53 nodes

## Key Concepts

- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **test_warded_indicator_in_websocket_room_updates()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_get_player_occupants_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_fallback_npc_method()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_empty()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_filters_dead()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_wrong_room()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_no_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_filters_dead()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_no_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event_with_drops()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_update_player_room_subscription_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_update_player_room_subscription_same_room()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_update_player_room_subscription_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_room_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_handles_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- *... and 28 more nodes in this community*

## Relationships

- [NPC Service Tests](NPC_Service_Tests.md) (22 shared connections)
- [Look Display Helpers](Look_Display_Helpers.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [API Type Guards](API_Type_Guards.md) (2 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`

## Audit Trail

- EXTRACTED: 142 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*