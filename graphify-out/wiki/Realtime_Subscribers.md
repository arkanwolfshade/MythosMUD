# Realtime Subscribers

> 447 nodes

## Key Concepts

- **EventBus** (159 connections) — `server/events/event_bus.py`
- **event_types.py** (86 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (85 connections) — `server/events/event_types.py`
- **NPCSpawningService** (67 connections) — `server/npc/spawning_service.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **PlayerLeftRoom** (57 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (56 connections) — `server/events/event_types.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCLeftRoom** (52 connections) — `server/events/event_types.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_bus.py** (31 connections) — `server/events/event_bus.py`
- **room.py** (30 connections) — `server/models/room.py`
- **event_reaction_system.py** (29 connections) — `server/npc/event_reaction_system.py`
- **movement_service.py** (28 connections) — `server/game/movement_service.py`
- **follow_service.py** (25 connections) — `server/game/follow_service.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **NPCEventReaction** (20 connections) — `server/npc/event_reaction_system.py`
- **movement_integration.py** (19 connections) — `server/npc/movement_integration.py`
- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **NPCAttacked** (16 connections) — `server/events/event_types.py`
- *... and 422 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (145 shared connections)
- [item models rationale](item_models_rationale.md) (72 shared connections)
- [command parser rationale](command_parser_rationale.md) (68 shared connections)
- [Loot Generation](Loot_Generation.md) (47 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (30 shared connections)
- [party service game](party_service_game.md) (24 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (19 shared connections)
- [player death service](player_death_service.md) (18 shared connections)
- [NPC Combat](NPC_Combat.md) (17 shared connections)
- [Database Config](Database_Config.md) (15 shared connections)
- [room models instance](room_models_instance.md) (15 shared connections)
- [party game service](party_game_service.md) (14 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/game/instance_manager.py`
- `server/game/movement_service.py`
- `server/game/quest/quest_events.py`
- `server/models/room.py`
- `server/npc/event_reaction_system.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/npc_event_handlers.py`
- `server/services/combat_hp_sync.py`
- `server/services/npc_instance_service.py`
- `server/services/npc_startup_service.py`
- `server/services/room_sync_service.py`

## Audit Trail

- EXTRACTED: 2103 (91%)
- INFERRED: 206 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*