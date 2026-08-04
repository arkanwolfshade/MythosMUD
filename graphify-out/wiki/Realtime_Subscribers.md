# Realtime Subscribers

> 425 nodes

## Key Concepts

- **event_types.py** (86 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (85 connections) — `server/events/event_types.py`
- **NPCLifecycleManager** (78 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **PlayerLeftRoom** (57 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (56 connections) — `server/events/event_types.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCLeftRoom** (52 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **NPCDied** (35 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **room.py** (30 connections) — `server/models/room.py`
- **event_reaction_system.py** (29 connections) — `server/npc/event_reaction_system.py`
- **NPCEventReactionSystem** (27 connections) — `server/npc/event_reaction_system.py`
- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **NPCEventReaction** (20 connections) — `server/npc/event_reaction_system.py`
- *... and 400 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (104 shared connections)
- [NPC Combat](NPC_Combat.md) (63 shared connections)
- [item models rationale](item_models_rationale.md) (44 shared connections)
- [container events rationale](container_events_rationale.md) (33 shared connections)
- [nats services service](nats_services_service.md) (26 shared connections)
- [combat services rationale](combat_services_rationale.md) (24 shared connections)
- [npc event handlers](npc_event_handlers.md) (21 shared connections)
- [models npc rationale](models_npc_rationale.md) (20 shared connections)
- [command service commands](command_service_commands.md) (19 shared connections)
- [party service game](party_service_game.md) (19 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (17 shared connections)
- [commands communication channels](commands_communication_channels.md) (17 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/population_control.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/event_handler.py`
- `server/realtime/integration/room_event_handler.py`

## Audit Trail

- EXTRACTED: 2106 (89%)
- INFERRED: 262 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*