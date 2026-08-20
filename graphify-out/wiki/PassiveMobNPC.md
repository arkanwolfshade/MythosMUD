# PassiveMobNPC

> 104 nodes

## Key Concepts

- **PassiveMobNPC** (57 connections) — `server/npc/passive_mob_npc.py`
- **test_npc_base.py** (25 connections) — `server/tests/unit/npc/test_npc_base.py`
- **NPCEventReactionSystem** (24 connections) — `server/npc/event_reaction_system.py`
- **test_passive_mob_npc.py** (20 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **passive_mob_npc.py** (18 connections) — `server/npc/passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **Any** (6 connections)
- **.__init__()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **.execute()** (4 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **.should_trigger()** (4 connections) — `server/npc/event_reaction_system.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **._handle_event()** (4 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **.get_npc_reaction_stats()** (3 connections) — `server/npc/event_reaction_system.py`
- **.register_npc_reactions()** (3 connections) — `server/npc/event_reaction_system.py`
- **.set_npc_context()** (3 connections) — `server/npc/event_reaction_system.py`
- **._subscribe_to_events()** (3 connections) — `server/npc/event_reaction_system.py`
- **._handle_respond_to_greeting()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.respond_to_player()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._setup_passive_mob_behavior_rules()** (3 connections) — `server/npc/passive_mob_npc.py`
- *... and 79 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (12 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (9 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (3 shared connections)
- [NPCBase](NPCBase.md) (3 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (3 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (1 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (1 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (1 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`
- `server/npc/passive_mob_npc.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_base.py`
- `server/tests/unit/npc/test_passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 179 (90%)
- INFERRED: 21 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*