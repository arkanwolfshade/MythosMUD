# RoomSubscriptionManager

> 79 nodes

## Key Concepts

- **RoomSubscriptionManager** (62 connections) — `server/realtime/room_subscription_manager.py`
- **InstanceFlushService** (29 connections) — `server/services/instance_flush_service.py`
- **test_instance_flush_service.py** (26 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **FakeBankPersistence** (16 connections) — `server/tests/unit/services/test_instance_flush_service.py`
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
- **._add_npc_to_occupants()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **test_flush_with_empty_floor_only_destroys()** (6 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **.add_room_drop()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **.take_room_drop()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **._filter_fallback_npcs()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/room_subscription_manager.py`
- *... and 54 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [ContainerCreateParams](ContainerCreateParams.md) (6 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (5 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (5 shared connections)
- [MessageQueue](MessageQueue.md) (4 shared connections)
- [NpcDisposition](NpcDisposition.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (2 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (2 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (2 shared connections)
- [test_room_subscription_manager.py](test_room_subscription_manager.py.md) (2 shared connections)

## Source Files

- `server/realtime/room_subscription_manager.py`
- `server/services/instance_flush_service.py`
- `server/tests/unit/services/test_instance_flush_service.py`

## Audit Trail

- EXTRACTED: 192 (84%)
- INFERRED: 37 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*