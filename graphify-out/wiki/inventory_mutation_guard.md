# inventory mutation guard

> 359 nodes

## Key Concepts

- **event_types.py** (86 connections) — `server/events/event_types.py`
- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **NPCDied** (35 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **event_bus.py** (31 connections) — `server/events/event_bus.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **DistributedEventBus** (22 connections) — `server/events/distributed_event_bus.py`
- **PlayerRespawnedEvent** (20 connections) — `server/events/event_types.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **NPCLifecycleRecord** (19 connections) — `server/npc/lifecycle_types.py`
- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **RoomOccupantsRefreshRequested** (17 connections) — `server/events/event_types.py`
- **_SpawnTrackedNPC** (17 connections) — `server/npc/lifecycle_manager.py`
- **NPCSpoke** (16 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- *... and 334 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (110 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (37 shared connections)
- [services nats service](services_nats_service.md) (32 shared connections)
- [wearable container service](wearable_container_service.md) (24 shared connections)
- [profession models rationale](profession_models_rationale.md) (23 shared connections)
- [Database Config](Database_Config.md) (19 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (15 shared connections)
- [NATS Messaging](NATS_Messaging.md) (13 shared connections)
- [player service game](player_service_game.md) (12 shared connections)
- [command service commands](command_service_commands.md) (12 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (11 shared connections)
- [player room realtime](player_room_realtime.md) (11 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_hp_sync.py`
- `server/services/room_sync_service.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_nats_event_bridge.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 1461 (90%)
- INFERRED: 165 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*