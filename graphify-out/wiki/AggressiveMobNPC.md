# AggressiveMobNPC

> 96 nodes

## Key Concepts

- **AggressiveMobNPC** (33 connections) — `server/npc/aggressive_mob_npc.py`
- **NPCEventReactionSystem** (27 connections) — `server/npc/event_reaction_system.py`
- **test_aggressive_mob_npc.py** (23 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **aggressive_mob_npc.py** (18 connections) — `server/npc/aggressive_mob_npc.py`
- **_make_aggro()** (13 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **_RoomPersistence** (7 connections) — `server/npc/aggressive_mob_npc.py`
- **._attack_target_impl()** (6 connections) — `server/npc/aggressive_mob_npc.py`
- **._compute_player_context()** (5 connections) — `server/npc/aggressive_mob_npc.py`
- **.__init__()** (5 connections) — `server/npc/passive_mob_npc.py`
- **.attack_target()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._attack_via_combat_integration()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._enrich_behavior_context()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **._handle_event()** (4 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **.flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._get_attack_damage()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_attack_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.__init__()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._log_context_enriched()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- *... and 71 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (16 shared connections)
- [event_types.py](event_types.py.md) (16 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [register_default_reactions_for_npc](register_default_reactions_for_npc.md) (1 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/npc/event_reaction_system.py`
- `server/npc/passive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`

## Audit Trail

- EXTRACTED: 164 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*