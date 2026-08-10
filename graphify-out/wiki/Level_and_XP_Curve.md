# Level and XP Curve

> 499 nodes

## Key Concepts

- **EventBus** (129 connections) — `server/events/event_bus.py`
- **time.py** (89 connections) — `server/container/bundles/time.py`
- **NPCBase** (82 connections) — `server/npc/npc_base.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **event_types.py** (74 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **npc_base.py** (41 connections) — `server/npc/npc_base.py`
- **AggressiveMobNPC** (32 connections) — `server/npc/aggressive_mob_npc.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **room.py** (31 connections) — `server/models/room.py`
- **event_bus.py** (29 connections) — `server/events/event_bus.py`
- **PassiveMobNPC** (29 connections) — `server/npc/passive_mob_npc.py`
- **event_reaction_system.py** (27 connections) — `server/npc/event_reaction_system.py`
- **NPCDied** (25 connections) — `server/events/event_types.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **NPCThreadManager** (25 connections) — `server/npc/threading.py`
- **NPCMovementIntegration** (24 connections) — `server/npc/movement_integration.py`
- **lifecycle_death.py** (23 connections) — `server/npc/lifecycle_death.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **NPCEventReactionSystem** (21 connections) — `server/npc/event_reaction_system.py`
- *... and 474 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (84 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (80 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (71 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (45 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (44 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (37 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (25 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (24 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (17 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (16 shared connections)
- [Archive Advanced Chat](Archive_Advanced_Chat.md) (14 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (13 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/container/bundles/time.py`
- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/instance_manager.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behavior_engine.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/idle_movement.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`

## Audit Trail

- EXTRACTED: 2339 (91%)
- INFERRED: 236 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*