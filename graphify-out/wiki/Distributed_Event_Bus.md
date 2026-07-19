# Distributed Event Bus

> 245 nodes · cohesion 0.02

## Key Concepts

- **EventBus** (203 connections) — `server/events/event_bus.py`
- **PlayerEnteredRoom** (86 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (85 connections) — `server/events/event_types.py`
- **MovementService** (67 connections) — `server/game/movement_service.py`
- **BaseEvent** (64 connections) — `server/events/event_types.py`
- **event_types.py** (44 connections) — `server/events/event_types.py`
- **FollowService** (40 connections) — `server/game/follow_service.py`
- **npc_base.py** (38 connections) — `server/npc/npc_base.py`
- **population_control.py** (32 connections) — `server/npc/population_control.py`
- **event_reaction_system.py** (26 connections) — `server/npc/event_reaction_system.py`
- **room.py** (24 connections) — `server/models/room.py`
- **UUID** (21 connections) — `server/game/follow_service.py`
- **movement_integration.py** (18 connections) — `server/npc/movement_integration.py`
- **follow_service.py** (15 connections) — `server/game/follow_service.py`
- **DistributedEventBus** (14 connections) — `server/events/distributed_event_bus.py`
- **Any** (14 connections) — `server/game/follow_service.py`
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **_PopulationLifecycleManager** (13 connections) — `server/npc/population_control.py`
- **NPCDefinition** (13 connections) — `server/npc/population_control.py`
- **nats_event_bridge.py** (12 connections) — `server/events/nats_event_bridge.py`
- **communication_integration.py** (11 connections) — `server/npc/communication_integration.py`
- **shopkeeper_npc.py** (11 connections) — `server/npc/shopkeeper_npc.py`
- **Any** (11 connections) — `server/events/event_bus.py`
- **__init__.py** (11 connections) — `server/events/__init__.py`
- **distributed_event_bus.py** (10 connections) — `server/events/distributed_event_bus.py`
- *... and 220 more nodes in this community*

## Relationships

- [[NPC Services Bundle]] (135 shared connections)
- [[NPC Death Lifecycle]] (55 shared connections)
- [[NPC Admin API]] (51 shared connections)
- [[Combat Service Bundle]] (24 shared connections)
- [[Aggressive Mob NPC]] (22 shared connections)
- [[Event Bus Serialization]] (20 shared connections)
- [[Player Movement Service]] (19 shared connections)
- [[Player Respawn Events]] (18 shared connections)
- [[Combat Command Handler]] (16 shared connections)
- [[Room Occupant Events]] (15 shared connections)
- [[Game Service Bundle]] (15 shared connections)
- [[NPC Combat Events]] (14 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/game/follow_service.py`
- `server/game/movement_service.py`
- `server/models/room.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/shopkeeper_npc.py`
- `server/tests/integration/test_follow_flow.py`

## Audit Trail

- EXTRACTED: 1138 (71%)
- INFERRED: 467 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
