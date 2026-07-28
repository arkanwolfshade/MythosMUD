# Server Realtime (14)

> 85 nodes

## Key Concepts

- **RoomSubscriptionManager** (41 connections) — `server/realtime/room_subscription_manager.py`
- **room_subscription_manager.py** (16 connections) — `server/realtime/room_subscription_manager.py`
- **room_event_handler.py** (13 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **test_room_subscription_manager_npcs.py** (13 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- **RoomEventHandler** (11 connections) — `server/realtime/integration/room_event_handler.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
- **._add_npc_to_occupants()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.list_room_drops()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.take_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_online_player_occupants()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._filter_fallback_npcs()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.reconcile_room_presence()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (3 connections)
- **.set_async_persistence()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.subscribe_to_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- *... and 60 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (8 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (6 shared connections)
- [Server Realtime (43)](Server_Realtime_%2843%29.md) (5 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (4 shared connections)
- [Server Events](Server_Events.md) (4 shared connections)
- [Server Npc](Server_Npc.md) (3 shared connections)
- [Server Realtime (109)](Server_Realtime_%28109%29.md) (3 shared connections)
- [Server Realtime (55)](Server_Realtime_%2855%29.md) (3 shared connections)
- [Server Realtime (64)](Server_Realtime_%2864%29.md) (2 shared connections)
- [Server Realtime (117)](Server_Realtime_%28117%29.md) (2 shared connections)
- [Server Realtime (44)](Server_Realtime_%2844%29.md) (1 shared connections)
- [Server Realtime (51)](Server_Realtime_%2851%29.md) (1 shared connections)

## Source Files

- `server/realtime/integration/__init__.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 285 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*