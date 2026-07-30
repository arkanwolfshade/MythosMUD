# combat initialization

> 114 nodes

## Key Concepts

- **BaseEvent** (73 connections) — `server/events/event_types.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **DistributedEventBus** (12 connections) — `server/events/distributed_event_bus.py`
- **event_serialization.py** (12 connections) — `server/events/event_serialization.py`
- **distributed_event_bus.py** (10 connections) — `server/events/distributed_event_bus.py`
- **Any** (10 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **test_nats_event_bridge.py** (7 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **._create_async_subscriber_tasks()** (6 connections) — `server/events/event_bus.py`
- **.unsubscribe()** (6 connections) — `server/events/event_bus.py`
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **._separate_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._process_sync_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._wait_for_async_subscribers()** (5 connections) — `server/events/event_bus.py`
- **.subscribe()** (5 connections) — `server/events/event_bus.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- *... and 89 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (49 shared connections)
- [Any](Any.md) (11 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (9 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [world](world.md) (5 shared connections)
- [get current tick()](get_current_tick%28%29.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (3 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (3 shared connections)
- [combat taunt](combat_taunt.md) (3 shared connections)
- [test event bus](test_event_bus.md) (2 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 418 (92%)
- INFERRED: 37 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*