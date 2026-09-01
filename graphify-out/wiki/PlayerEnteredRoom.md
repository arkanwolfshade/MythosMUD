# PlayerEnteredRoom

> 143 nodes

## Key Concepts

- **PlayerEnteredRoom** (77 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **NPCEventReaction** (21 connections) — `server/npc/event_reaction_system.py`
- **register_default_reactions_for_npc()** (17 connections) — `server/npc/npc_default_reactions.py`
- **test_quest_events.py** (17 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_event_handlers_room_left.py** (16 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **NPCEventReactionTemplates** (14 connections) — `server/npc/event_reaction_system.py`
- **asyncio** (11 connections)
- **npc_default_reactions.py** (10 connections) — `server/npc/npc_default_reactions.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **test_farewell_and_spoke_reactions_schedule_speech()** (7 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **_make_on_player_left()** (6 connections) — `server/game/quest/quest_events.py`
- **.player_entered_room_greeting()** (6 connections) — `server/npc/event_reaction_system.py`
- **Any** (6 connections)
- **.npc_attacked_retaliation()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_left_room_farewell()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_spoke_response()** (5 connections) — `server/npc/event_reaction_system.py`
- **test_npc_died_no_killer_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_invalid_player_id_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- *... and 118 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (45 shared connections)
- [event_types.py](event_types.py.md) (29 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (10 shared connections)
- [FollowService](FollowService.md) (9 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (8 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (5 shared connections)
- [test_population_control.py](test_population_control.py.md) (4 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [PlayerXPAwardEvent](PlayerXPAwardEvent.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/game/quest/quest_events.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/spawning_service.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`

## Audit Trail

- EXTRACTED: 325 (86%)
- INFERRED: 52 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*