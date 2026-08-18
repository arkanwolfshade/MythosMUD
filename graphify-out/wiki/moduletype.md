# moduletype

> 301 nodes

## Key Concepts

- **EventBus** (207 connections) — `server/events/event_bus.py`
- **BaseEvent** (93 connections) — `server/events/event_types.py`
- **test_event_bus.py** (60 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **event_serialization.py** (20 connections) — `server/events/event_serialization.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_distributed_event_bus.py** (16 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_event_serialization.py** (16 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **test_party_flow.py** (14 connections) — `server/tests/integration/test_party_flow.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **distributed_event_bus.py** (12 connections) — `server/events/distributed_event_bus.py`
- **PartyUpdated** (11 connections) — `server/events/event_types.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **._stop_processing()** (7 connections) — `server/events/event_bus.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 276 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (77 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (29 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (12 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (10 shared connections)
- [server events combat events](server_events_combat_events.md) (8 shared connections)
- [server game party service partyservice](server_game_party_service_partyservice.md) (8 shared connections)
- [server events event types npcdied](server_events_event_types_npcdied.md) (6 shared connections)
- [server events combat events combatendedevent](server_events_combat_events_combatendedevent.md) (5 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (5 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (4 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (4 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (4 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/game/movement_service.py`
- `server/npc/event_reaction_system.py`
- `server/npc/passive_mob_npc.py`
- `server/realtime/connection_manager.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 636 (83%)
- INFERRED: 127 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*