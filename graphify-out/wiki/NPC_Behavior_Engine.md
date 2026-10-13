# NPC Behavior Engine

> 310 nodes

## Key Concepts

- **NPCDefinition** (112 connections) — `server/models/npc.py`
- **NPCBase** (75 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (62 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (47 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **NPCEventReactionSystem** (43 connections) — `server/npc/event_reaction_system.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **spawning_service.py** (40 connections) — `server/npc/spawning_service.py`
- **models/npc.py** (38 connections) — `server/models/npc.py`
- **event_reaction_system.py** (36 connections) — `server/npc/event_reaction_system.py`
- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **npc_instance_service.py** (28 connections) — `server/services/npc_instance_service.py`
- **npc_base.py** (27 connections) — `server/npc/npc_base.py`
- **spawning_instance_factory.py** (27 connections) — `server/npc/spawning_instance_factory.py`
- **server/events/__init__.py** (26 connections) — `server/events/__init__.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **bundles/npc.py** (20 connections) — `server/container/bundles/npc.py`
- **aggressive_mob_npc.py** (20 connections) — `server/npc/aggressive_mob_npc.py`
- **combat_integration.py** (20 connections) — `server/npc/combat_integration.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **SimpleNPCDefinition** (19 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (19 connections) — `server/npc/spawning_instance_factory.py`
- **server/npc/__init__.py** (19 connections) — `server/npc/__init__.py`
- **passive_mob_npc.py** (19 connections) — `server/npc/passive_mob_npc.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- *... and 285 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (63 shared connections)
- [Game Event Types](Game_Event_Types.md) (56 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (51 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (31 shared connections)
- [NPC Definition JSON](NPC_Definition_JSON.md) (30 shared connections)
- [Community 40](Community_40.md) (25 shared connections)
- [Community 53](Community_53.md) (20 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (18 shared connections)
- [Community 48](Community_48.md) (17 shared connections)
- [Community 276](Community_276.md) (15 shared connections)
- [NPC Population Stats](NPC_Population_Stats.md) (11 shared connections)
- [Community 77](Community_77.md) (11 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/event_types.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`

## Audit Trail

- EXTRACTED: 987 (94%)
- INFERRED: 67 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*