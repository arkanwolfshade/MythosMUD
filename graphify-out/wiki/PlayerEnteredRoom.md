# PlayerEnteredRoom

> 197 nodes

## Key Concepts

- **PlayerEnteredRoom** (91 connections) — `server/events/event_types.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **PlayerLeftRoom** (56 connections) — `server/events/event_types.py`
- **NPCEventReaction** (23 connections) — `server/npc/event_reaction_system.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **register_default_reactions_for_npc()** (20 connections) — `server/npc/npc_default_reactions.py`
- **test_quest_events.py** (17 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_reaction_revival_integration.py** (17 connections) — `server/tests/unit/npc/test_reaction_revival_integration.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **NPCEventReactionTemplates** (14 connections) — `server/npc/event_reaction_system.py`
- **test_npc_default_reactions.py** (11 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **build_corruption_aware_greeting()** (10 connections) — `server/npc/corruption_reactions.py`
- **_shopkeeper()** (9 connections) — `server/tests/unit/npc/test_reaction_revival_integration.py`
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (7 connections) — `server/game/quest/quest_events.py`
- **test_farewell_and_spoke_reactions_schedule_speech()** (7 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_greeting_respects_the_per_npc_per_event_cooldown()** (6 connections) — `server/tests/unit/npc/test_reaction_revival_integration.py`
- **test_no_reactions_registered_without_a_reaction_system()** (6 connections) — `server/tests/unit/npc/test_reaction_revival_integration.py`
- **asyncio** (6 connections)
- **.npc_attacked_retaliation()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_entered_room_greeting()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_left_room_farewell()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_spoke_response()** (5 connections) — `server/npc/event_reaction_system.py`
- *... and 172 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (75 shared connections)
- [event_handler.py](event_handler.py.md) (10 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (10 shared connections)
- [FollowService](FollowService.md) (9 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (8 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (8 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (7 shared connections)
- [CorruptionTier](CorruptionTier.md) (6 shared connections)
- [NpcDisposition](NpcDisposition.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (6 shared connections)
- [test_player_event_handlers_room_left.py](test_player_event_handlers_room_left.py.md) (6 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/game/quest/quest_events.py`
- `server/npc/corruption_reactions.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/spawning_service.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_corruption_reactions.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_reaction_revival_integration.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`
- `server/tests/unit/realtime/test_room_system_message_categories.py`

## Audit Trail

- EXTRACTED: 451 (89%)
- INFERRED: 57 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*