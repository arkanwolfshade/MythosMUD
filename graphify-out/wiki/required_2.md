# required

> 21 nodes

## Key Concepts

- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **test_distributed_event_bus.py** (16 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **asyncio** (6 connections)
- **SampleEvent** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_with_nats_bridge_publishes_to_nats()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_without_nats_delegates_to_parent()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_starts_bridge_when_loop_running()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_bridge_stop_error_is_swallowed()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_stops_bridge()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_distributed_event_bus_init_without_nats()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_same_reference_noop()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **EventBus that distributes domain events via NATS for horizontal scaling. When…** (1 connections) — `server/events/distributed_event_bus.py`
- **Unit tests for DistributedEventBus.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Minimal event for distributed bus tests.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Single-instance mode has no bridge until NATS is set.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Setting the same NATS service twice does not recreate the bridge.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Publish without NATS behaves like plain EventBus.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **When bridge is active, publish also sends to NATS.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Shutdown awaits bridge stop before parent shutdown.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Bridge stop errors do not prevent shutdown.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **set_nats_service creates bridge and schedules start when loop is running.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`

## Relationships

- [NPCDefinition](NPCDefinition.md) (6 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [player_respawned Event Payload Gap](player_respawned_Event_Payload_Gap.md) (2 shared connections)
- [Logging Best Practices](Logging_Best_Practices.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [long_description](long_description.md) (1 shared connections)
- [test_parse_exits_json_string_valid](test_parse_exits_json_string_valid.md) (1 shared connections)
- [pylint.py](pylint.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/tests/unit/events/test_distributed_event_bus.py`

## Audit Trail

- EXTRACTED: 44 (85%)
- INFERRED: 8 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*