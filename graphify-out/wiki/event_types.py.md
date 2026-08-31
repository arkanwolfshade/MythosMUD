# event_types.py

> 333 nodes

## Key Concepts

- **event_types.py** (94 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (77 connections) — `server/events/event_types.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **NPCEnteredRoom** (47 connections) — `server/events/event_types.py`
- **FollowService** (45 connections) — `server/game/follow_service.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **test_event_handler.py** (42 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **event_handler.py** (36 connections) — `server/realtime/event_handler.py`
- **follow_service.py** (32 connections) — `server/game/follow_service.py`
- **models/room.py** (32 connections) — `server/models/room.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **follow_movement.py** (28 connections) — `server/game/follow_movement.py`
- **server/events/__init__.py** (25 connections) — `server/events/__init__.py`
- **RoomSyncService** (21 connections) — `server/services/room_sync_service.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **_FollowMovementHost** (20 connections) — `server/game/follow_movement.py`
- **movement_integration.py** (20 connections) — `server/npc/movement_integration.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **room_sync_service.py** (18 connections) — `server/services/room_sync_service.py`
- **npc_event_handlers.py** (17 connections) — `server/realtime/npc_event_handlers.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- *... and 308 more nodes in this community*

## Relationships

- [NPCLifecycleManager](NPCLifecycleManager.md) (64 shared connections)
- [EventBus](EventBus.md) (46 shared connections)
- [NPCBase](NPCBase.md) (36 shared connections)
- [get_logger](get_logger.md) (35 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (31 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (23 shared connections)
- [test_event_reaction_speech.py](test_event_reaction_speech.py.md) (17 shared connections)
- [MessageBuilder](MessageBuilder.md) (15 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (14 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (14 shared connections)
- [PlayerXPAwardEvent](PlayerXPAwardEvent.md) (13 shared connections)
- [Room](Room.md) (11 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/game/instance_manager.py`
- `server/models/room.py`
- `server/npc/event_reaction_system.py`
- `server/npc/movement_integration.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/events/test_nats_event_bridge.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 1040 (89%)
- INFERRED: 127 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*