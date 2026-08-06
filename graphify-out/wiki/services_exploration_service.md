# services exploration service

> 16 nodes

## Key Concepts

- **MockEventClass** (35 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_not_found()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_multiple_handlers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_isolates_sync_subscriber_errors()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_async_subscriber_error_isolation()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_and_get_all_counts()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_and_publish_when_running()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_queue_full_raises()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Mock event class for testing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() when handler not found.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() queues or processes event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() with multiple handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() removes all handlers for a service.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [event bus events](event_bus_events.md) (11 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [game room service](game_room_service.md) (2 shared connections)
- [room toolkit validator](room_toolkit_validator.md) (2 shared connections)
- [realtime player event](realtime_player_event.md) (2 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (1 shared connections)
- [services chat rate](services_chat_rate.md) (1 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (1 shared connections)
- [infrastructure security rationale](infrastructure_security_rationale.md) (1 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (1 shared connections)
- [realtime messaging message](realtime_messaging_message.md) (1 shared connections)
- [events event bus](events_event_bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 29 (45%)
- INFERRED: 35 (55%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*