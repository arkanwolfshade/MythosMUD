# NPCEventReaction

> 58 nodes

## Key Concepts

- **NPCEventReaction** (21 connections) — `server/npc/event_reaction_system.py`
- **register_default_reactions_for_npc()** (17 connections) — `server/npc/npc_default_reactions.py`
- **NPCEventReactionTemplates** (14 connections) — `server/npc/event_reaction_system.py`
- **npc_default_reactions.py** (10 connections) — `server/npc/npc_default_reactions.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_farewell_and_spoke_reactions_schedule_speech()** (7 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **.player_entered_room_greeting()** (6 connections) — `server/npc/event_reaction_system.py`
- **Any** (6 connections)
- **.npc_attacked_retaliation()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_left_room_farewell()** (5 connections) — `server/npc/event_reaction_system.py`
- **.player_spoke_response()** (5 connections) — `server/npc/event_reaction_system.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **test_greeting_reaction_schedules_npc_speech()** (5 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_greeting_reaction_skips_unknown_room()** (5 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **.execute()** (4 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **.should_trigger()** (4 connections) — `server/npc/event_reaction_system.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **._handle_event()** (4 connections) — `server/npc/event_reaction_system.py`
- **test_npc_event_reaction_action_error_returns_false()** (4 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_npc_event_reaction_condition_error_returns_false()** (4 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_npc_event_reaction_no_action_returns_true()** (4 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_npc_event_reaction_no_condition_defaults_true()** (4 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **.get_npc_reaction_stats()** (3 connections) — `server/npc/event_reaction_system.py`
- **.register_npc_reactions()** (3 connections) — `server/npc/event_reaction_system.py`
- *... and 33 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (28 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (7 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [npc_config_parsing.py](npc_config_parsing.py.md) (1 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (1 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 119 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*