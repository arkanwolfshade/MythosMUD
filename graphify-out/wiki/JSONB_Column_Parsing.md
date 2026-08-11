# JSONB Column Parsing

> 74 nodes

## Key Concepts

- **RoomSubscriptionManager** (44 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **test_room_subscription_manager_npcs.py** (13 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **._add_npc_to_occupants()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.list_room_drops()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.take_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_online_player_occupants()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._filter_fallback_npcs()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.reconcile_room_presence()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.set_async_persistence()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.subscribe_to_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.unsubscribe_from_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.get_room_subscribers()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.adjust_room_drop()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_occupant()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.remove_room_occupant()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.get_stats()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **subscription_manager()** (3 connections) — `server/tests/unit/realtime/test_room_subscription_manager_drops.py`
- *... and 49 more nodes in this community*

## Relationships

- [Players API Endpoints](Players_API_Endpoints.md) (6 shared connections)
- [NATS Subject Patterns](NATS_Subject_Patterns.md) (4 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (2 shared connections)
- [App Router Integration](App_Router_Integration.md) (2 shared connections)
- [Game Status API](Game_Status_API.md) (2 shared connections)
- [NATS Subject Validator](NATS_Subject_Validator.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (1 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_room_subscription_manager_drops.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 228 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*