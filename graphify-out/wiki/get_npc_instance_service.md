# get_npc_instance_service

> 454 nodes

## Key Concepts

- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **event_types.py** (74 connections) — `server/events/event_types.py`
- **NPCLifecycleManager** (73 connections) — `server/npc/lifecycle_manager.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **NPCPopulationController** (62 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCSpawningService** (48 connections) — `server/npc/spawning_service.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **NPCEnteredRoom** (43 connections) — `server/events/event_types.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **NPCLeftRoom** (40 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (40 connections) — `server/events/event_types.py`
- **PlayerDPUpdated** (37 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **models/room.py** (31 connections) — `server/models/room.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **NPCThreadManager** (25 connections) — `server/npc/threading.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **lifecycle_death.py** (23 connections) — `server/npc/lifecycle_death.py`
- **asyncio** (23 connections)
- **NPCDied** (22 connections) — `server/events/event_types.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- *... and 429 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (130 shared connections)
- [get_logger](get_logger.md) (62 shared connections)
- [ConnectionManager](ConnectionManager.md) (38 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (24 shared connections)
- [BaseEvent](BaseEvent.md) (22 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (22 shared connections)
- [test_npc_combat_integration_class.py](test_npc_combat_integration_class.py.md) (22 shared connections)
- [threading.py](threading.py.md) (21 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (18 shared connections)
- [.__post_init__](__post_init__.md) (16 shared connections)
- [alias_storage.py](alias_storage.py.md) (16 shared connections)
- [test_population_control.py](test_population_control.py.md) (15 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/commands/combat_handler.py`
- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`

## Audit Trail

- EXTRACTED: 2131 (92%)
- INFERRED: 177 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*