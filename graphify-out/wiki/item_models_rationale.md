# item models rationale

> 207 nodes

## Key Concepts

- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **DistributedEventBus** (22 connections) — `server/events/distributed_event_bus.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **test_distributed_event_bus.py** (14 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **event_serialization.py** (12 connections) — `server/events/event_serialization.py`
- **distributed_event_bus.py** (11 connections) — `server/events/distributed_event_bus.py`
- **Any** (10 connections)
- **test_nats_event_bridge.py** (9 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **._create_async_subscriber_tasks()** (6 connections) — `server/events/event_bus.py`
- **.unsubscribe()** (6 connections) — `server/events/event_bus.py`
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **Any** (6 connections)
- **._handle_event()** (6 connections) — `server/npc/event_reaction_system.py`
- **SampleEvent** (6 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **._separate_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._process_sync_subscribers()** (5 connections) — `server/events/event_bus.py`
- *... and 182 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (72 shared connections)
- [NPC Combat](NPC_Combat.md) (12 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (10 shared connections)
- [player death service](player_death_service.md) (6 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [schedule services service](schedule_services_service.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [command parser rationale](command_parser_rationale.md) (3 shared connections)
- [combat validator validators](combat_validator_validators.md) (3 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [feature services flag](feature_services_flag.md) (3 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/event_reaction_system.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 685 (93%)
- INFERRED: 53 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*