# Realtime Messaging Message

> 52 nodes · cohesion 0.06

## Key Concepts

- **RoomSubscriptionManager** (45 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **._add_npc_to_occupants()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **mock_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.add_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._filter_fallback_npcs()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_online_player_occupants()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.list_room_drops()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.reconcile_room_presence()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.take_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_occupant()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.adjust_room_drop()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.get_room_subscribers()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.get_stats()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.remove_room_occupant()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.set_async_persistence()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.subscribe_to_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.unsubscribe_from_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.__init__()** (2 connections) — `server/realtime/room_subscription_manager.py`
- *... and 27 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (4 shared connections)
- [Npc Communication](Npc_Communication.md) (2 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (2 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (2 shared connections)
- [Target Resolution Service](Target_Resolution_Service.md) (2 shared connections)
- [Respawn Persistence Bug](Respawn_Persistence_Bug.md) (2 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (1 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)
- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`

## Audit Trail

- EXTRACTED: 182 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*