# services nats service

> 237 nodes

## Key Concepts

- **NPCCombatIntegration** (103 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (46 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **event_reaction_system.py** (29 connections) — `server/npc/event_reaction_system.py`
- **NPCEventReactionSystem** (27 connections) — `server/npc/event_reaction_system.py`
- **combat_integration.py** (26 connections) — `server/npc/combat_integration.py`
- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **combat_integration_base.py** (21 connections) — `server/npc/combat_integration_base.py`
- **NPCEventReaction** (20 connections) — `server/npc/event_reaction_system.py`
- **aggressive_mob_npc.py** (18 connections) — `server/npc/aggressive_mob_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **NPCAttacked** (16 connections) — `server/events/event_types.py`
- **register_default_reactions_for_npc()** (15 connections) — `server/npc/npc_default_reactions.py`
- **NPCListened** (14 connections) — `server/events/event_types.py`
- **shopkeeper_npc.py** (12 connections) — `server/npc/shopkeeper_npc.py`
- **npc_default_reactions.py** (10 connections) — `server/npc/npc_default_reactions.py`
- **NPCEventReactionTemplates** (9 connections) — `server/npc/event_reaction_system.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **_RoomPersistence** (8 connections) — `server/npc/aggressive_mob_npc.py`
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **UUID** (7 connections)
- **.get_combat_stats()** (7 connections) — `server/npc/combat_integration.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- *... and 212 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (44 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (32 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (26 shared connections)
- [lucidity event services](lucidity_event_services.md) (18 shared connections)
- [room look commands](room_look_commands.md) (11 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (11 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (6 shared connections)
- [error logging rationale](error_logging_rationale.md) (5 shared connections)
- [grace period disconnect](grace_period_disconnect.md) (5 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [command exploration models](command_exploration_models.md) (4 shared connections)
- [command input commands](command_input_commands.md) (4 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/shopkeeper_npc.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 983 (96%)
- INFERRED: 40 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*