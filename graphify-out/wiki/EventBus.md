# EventBus

> 295 nodes

## Key Concepts

- **EventBus** (189 connections) — `server/events/event_bus.py`
- **BaseEvent** (96 connections) — `server/events/event_types.py`
- **event_types.py** (93 connections) — `server/events/event_types.py`
- **test_event_bus.py** (60 connections) — `server/tests/unit/events/test_event_bus.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **event_bus.py** (39 connections) — `server/events/event_bus.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **asyncio** (28 connections)
- **server/events/__init__.py** (25 connections) — `server/events/__init__.py`
- **event_serialization.py** (20 connections) — `server/events/event_serialization.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **EventBusProcessingMixin** (18 connections) — `server/events/event_bus_processing.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **room_sync_service.py** (18 connections) — `server/services/room_sync_service.py`
- **test_event_serialization.py** (16 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_follow_flow.py** (15 connections) — `server/tests/integration/test_follow_flow.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **NPCSpoke** (14 connections) — `server/events/event_types.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **communication_integration.py** (13 connections) — `server/npc/communication_integration.py`
- **NPCListened** (12 connections) — `server/events/event_types.py`
- **distributed_event_bus.py** (12 connections) — `server/events/distributed_event_bus.py`
- **EventBusMixinBase** (10 connections) — `server/events/event_bus_base.py`
- *... and 270 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (33 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (32 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (28 shared connections)
- [NPCEnteredRoom](NPCEnteredRoom.md) (27 shared connections)
- [NATSError](NATSError.md) (22 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (17 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (16 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (16 shared connections)
- [NPCBase](NPCBase.md) (16 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (12 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (12 shared connections)
- [PartyService](PartyService.md) (11 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_bus_base.py`
- `server/events/event_bus_lifecycle.py`
- `server/events/event_bus_processing.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/models/room.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/services/room_sync_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 846 (88%)
- INFERRED: 113 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*