# scripts worktree ops

> 33 nodes

## Key Concepts

- **DistributedEventBus** (22 connections) — `server/events/distributed_event_bus.py`
- **test_distributed_event_bus.py** (14 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **SampleEvent** (6 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- **test_publish_without_nats_delegates_to_parent()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_with_nats_bridge_publishes_to_nats()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.__init__()** (3 connections) — `server/events/distributed_event_bus.py`
- **.publish()** (3 connections) — `server/events/distributed_event_bus.py`
- **distributed_bus()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_distributed_event_bus_init_without_nats()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_same_reference_noop()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_stops_bridge()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_bridge_stop_error_is_swallowed()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_starts_bridge_when_loop_running()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Any** (2 connections)
- **.shutdown()** (2 connections) — `server/events/distributed_event_bus.py`
- **Initialize core services. No dependencies.** (1 connections) — `server/container/bundles/core.py`
- **EventBus that distributes domain events via NATS for horizontal scaling.      Wh** (1 connections) — `server/events/distributed_event_bus.py`
- **Initialize distributed EventBus.          Args:             nats_service: NATS s** (1 connections) — `server/events/distributed_event_bus.py`
- **Set NATS service and start the bridge (call after NATS connects).** (1 connections) — `server/events/distributed_event_bus.py`
- **Publish event locally and to NATS when bridge is active.** (1 connections) — `server/events/distributed_event_bus.py`
- **Shutdown EventBus and stop NATS bridge.** (1 connections) — `server/events/distributed_event_bus.py`
- **Unit tests for DistributedEventBus.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Minimal event for distributed bus tests.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- *... and 8 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (10 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (1 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)
- [tools generate invite](tools_generate_invite.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/events/distributed_event_bus.py`
- `server/tests/unit/events/test_distributed_event_bus.py`

## Audit Trail

- EXTRACTED: 101 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*