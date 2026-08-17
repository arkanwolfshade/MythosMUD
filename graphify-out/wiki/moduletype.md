# moduletype

> 115 nodes

## Key Concepts

- **BaseEvent** (79 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (46 connections) — `server/events/event_types.py`
- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **event_serialization.py** (20 connections) — `server/events/event_serialization.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_distributed_event_bus.py** (16 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_event_serialization.py** (16 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **distributed_event_bus.py** (12 connections) — `server/events/distributed_event_bus.py`
- **test_nats_event_bridge.py** (10 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **asyncio** (6 connections)
- **SampleEvent** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_publish_with_nats_bridge_publishes_to_nats()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_without_nats_delegates_to_parent()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_handle_nats_message_injects_remote_origin()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- *... and 90 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (26 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (15 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [server events combat events](server_events_combat_events.md) (10 shared connections)
- [server tests unit events test](server_tests_unit_events_test.md) (8 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (8 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (7 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (5 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (5 shared connections)
- [server events event types playerdiedevent](server_events_event_types_playerdiedevent.md) (4 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (4 shared connections)
- [followtargetvalue](followtargetvalue.md) (4 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 263 (81%)
- INFERRED: 63 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*