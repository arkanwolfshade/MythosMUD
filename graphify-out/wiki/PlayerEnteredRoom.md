# PlayerEnteredRoom

> 143 nodes

## Key Concepts

- **PlayerEnteredRoom** (76 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **NPCEventReaction** (21 connections) — `server/npc/event_reaction_system.py`
- **register_default_reactions_for_npc()** (17 connections) — `server/npc/npc_default_reactions.py`
- **test_quest_events.py** (17 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_event_handlers_room_left.py** (16 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **NPCEventReactionTemplates** (14 connections) — `server/npc/event_reaction_system.py`
- **asyncio** (11 connections)
- **npc_default_reactions.py** (10 connections) — `server/npc/npc_default_reactions.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **test_farewell_and_spoke_reactions_schedule_speech()** (7 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **_make_on_player_left()** (6 connections) — `server/game/quest/quest_events.py`
- **.player_entered_room_greeting()** (6 connections) — `server/npc/event_reaction_system.py`
- **.npc_attacked_retaliation()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_left_room_farewell()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_spoke_response()** (5 connections) — `server/npc/event_reaction_system.py`
- **test_npc_died_no_killer_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- *... and 118 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (28 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (26 shared connections)
- [NPCEnteredRoom](NPCEnteredRoom.md) (12 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (9 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (9 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (8 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (6 shared connections)
- [test_population_control.py](test_population_control.py.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [.__post_init__](__post_init__.md) (4 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_default_reactions.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`

## Audit Trail

- EXTRACTED: 331 (87%)
- INFERRED: 51 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*