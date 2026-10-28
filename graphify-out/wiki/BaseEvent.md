# BaseEvent

> 278 nodes · cohesion 0.01

## Key Concepts

- **event_types.py** (102 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (91 connections) — `server/events/event_types.py`
- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **models/room.py** (58 connections) — `server/models/room.py`
- **PlayerLeftRoom** (56 connections) — `server/events/event_types.py`
- **NPCEventReactionSystem** (47 connections) — `server/npc/event_reaction_system.py`
- **npc_base.py** (46 connections) — `server/npc/npc_base.py`
- **event_reaction_system.py** (36 connections) — `server/npc/event_reaction_system.py`
- **spawning_instance_factory.py** (27 connections) — `server/npc/spawning_instance_factory.py`
- **server/events/__init__.py** (26 connections) — `server/events/__init__.py`
- **NPCEventReaction** (23 connections) — `server/npc/event_reaction_system.py`
- **ShopkeeperNPC** (22 connections) — `server/npc/shopkeeper_npc.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **aggressive_mob_npc.py** (20 connections) — `server/npc/aggressive_mob_npc.py`
- **register_default_reactions_for_npc()** (20 connections) — `server/npc/npc_default_reactions.py`
- **server/npc/__init__.py** (19 connections) — `server/npc/__init__.py`
- **passive_mob_npc.py** (19 connections) — `server/npc/passive_mob_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **test_reaction_revival_integration.py** (17 connections) — `server/tests/unit/npc/test_reaction_revival_integration.py`
- **NPCSpoke** (14 connections) — `server/events/event_types.py`
- **NPCEventReactionTemplates** (14 connections) — `server/npc/event_reaction_system.py`
- **shopkeeper_npc.py** (14 connections) — `server/npc/shopkeeper_npc.py`
- **communication_integration.py** (13 connections) — `server/npc/communication_integration.py`
- **npc_default_reactions.py** (13 connections) — `server/npc/npc_default_reactions.py`
- **NPCListened** (12 connections) — `server/events/event_types.py`
- *... and 253 more nodes in this community*

## Relationships

- [Room](Room.md) (47 shared connections)
- [RoomLoader](RoomLoader.md) (44 shared connections)
- [get_username_from_user](get_username_from_user.md) (36 shared connections)
- [CombatInstance](CombatInstance.md) (31 shared connections)
- [SpellLearningService](SpellLearningService.md) (27 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (16 shared connections)
- [look_container.py](look_container.py.md) (15 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (12 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (11 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (10 shared connections)
- [Async Remediation Summary - December 3, 2025](Async_Remediation_Summary_-_December_3,_2025.md) (9 shared connections)
- [combat_assist.py](combat_assist.py.md) (8 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/npc_protocols.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 901 (92%)
- INFERRED: 80 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*