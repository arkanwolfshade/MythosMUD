# npc_base.py

> 131 nodes

## Key Concepts

- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **NPCEventReactionSystem** (24 connections) — `server/npc/event_reaction_system.py`
- **server/npc/__init__.py** (22 connections) — `server/npc/__init__.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **NPCEventReaction** (21 connections) — `server/npc/event_reaction_system.py`
- **passive_mob_npc.py** (20 connections) — `server/npc/passive_mob_npc.py`
- **aggressive_mob_npc.py** (19 connections) — `server/npc/aggressive_mob_npc.py`
- **register_default_reactions_for_npc()** (17 connections) — `server/npc/npc_default_reactions.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **NPCSpoke** (14 connections) — `server/events/event_types.py`
- **NPCEventReactionTemplates** (14 connections) — `server/npc/event_reaction_system.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **communication_integration.py** (13 connections) — `server/npc/communication_integration.py`
- **shopkeeper_npc.py** (13 connections) — `server/npc/shopkeeper_npc.py`
- **NPCListened** (12 connections) — `server/events/event_types.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **npc_default_reactions.py** (10 connections) — `server/npc/npc_default_reactions.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **NPCTookDamage** (7 connections) — `server/events/event_types.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **test_farewell_and_spoke_reactions_schedule_speech()** (7 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- *... and 106 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (44 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [NPCBase](NPCBase.md) (18 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (6 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (6 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [.__post_init__](__post_init__.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/shopkeeper_npc.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 372 (92%)
- INFERRED: 33 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*