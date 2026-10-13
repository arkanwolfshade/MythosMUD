# Community 155

> 83 nodes

## Key Concepts

- **RoomSubscriptionManager** (62 connections) — `server/realtime/room_subscription_manager.py`
- **InstanceFlushService** (29 connections) — `server/services/instance_flush_service.py`
- **test_instance_flush_service.py** (25 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **FakeBankPersistence** (15 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (13 connections)
- **_instance_manager()** (11 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_never_evicts_from_a_full_box()** (9 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **_stack()** (8 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_appends_to_an_existing_box()** (8 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_of_an_unknown_instance_with_leftover_drops_loses_them_without_raising()** (8 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_survives_database_errors()** (8 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **asyncio** (8 connections)
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **test_flush_all_flushes_every_live_instance_into_each_owners_box()** (7 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_sends_only_that_instances_drops_to_its_owners_box_then_destroys_it()** (7 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_with_a_malformed_owner_id_loses_the_items_without_raising()** (7 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **test_flush_with_empty_floor_only_destroys()** (6 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **._add_npc_to_occupants()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_drop()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **.take_room_drop()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._filter_fallback_npcs()** (4 connections) — `server/realtime/room_subscription_manager.py`
- *... and 58 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (24 shared connections)
- [Community 221](Community_221.md) (5 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (4 shared connections)
- [Community 127](Community_127.md) (3 shared connections)
- [Community 538](Community_538.md) (2 shared connections)
- [Connection Manager Broadcast](Connection_Manager_Broadcast.md) (2 shared connections)
- [Community 119](Community_119.md) (2 shared connections)
- [Community 501](Community_501.md) (2 shared connections)
- [Community 314](Community_314.md) (2 shared connections)
- [Community 256](Community_256.md) (2 shared connections)
- [Community 458](Community_458.md) (2 shared connections)
- [Community 698](Community_698.md) (2 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/room_subscription_manager.py`
- `server/services/instance_flush_service.py`
- `server/tests/unit/services/test_instance_flush_service.py`

## Audit Trail

- EXTRACTED: 194 (85%)
- INFERRED: 35 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*