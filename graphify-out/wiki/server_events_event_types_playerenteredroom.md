# server events event types playerenteredroom

> 82 nodes

## Key Concepts

- **PlayerEnteredRoom** (62 connections) — `server/events/event_types.py`
- **NPCEventReactionSystem** (24 connections) — `server/npc/event_reaction_system.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
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
- **test_greeting_reaction_schedules_npc_speech()** (5 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_greeting_reaction_skips_unknown_room()** (5 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_handle_event_respects_cooldown()** (5 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_npc_attacked_retaliation_template()** (5 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_npc_event_reaction_wrong_event_type()** (5 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **test_register_handle_event_and_stats()** (5 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **.execute()** (4 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **.should_trigger()** (4 connections) — `server/npc/event_reaction_system.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **._handle_event()** (4 connections) — `server/npc/event_reaction_system.py`
- *... and 57 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (19 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (11 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (7 shared connections)
- [moduletype](moduletype.md) (7 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [followtargetvalue](followtargetvalue.md) (4 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (4 shared connections)
- [server npc init](server_npc_init.md) (4 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (3 shared connections)
- [server tests integration test follow](server_tests_integration_test_follow.md) (2 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_default_reactions.py`
- `server/realtime/event_handler.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 170 (77%)
- INFERRED: 51 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*