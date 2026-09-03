# Test Quest Events

> 41 nodes

## Key Concepts

- **test_quest_events.py** (17 connections) — `server/tests/unit/game/test_quest_events.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (6 connections) — `server/game/quest/quest_events.py`
- **test_npc_died_no_killer_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_invalid_player_id_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_starts_quest_by_room_trigger()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_left_records_exit_activity()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **asyncio** (5 connections)
- **._on_player_entered_room()** (4 connections) — `server/game/follow_service.py`
- **_entity_id_for_quest_offer()** (4 connections) — `server/game/quest/quest_events.py`
- **_parse_player_id()** (4 connections) — `server/game/quest/quest_events.py`
- **Any** (4 connections)
- **test_entity_id_for_quest_offer_plain_room_unchanged()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_entity_id_for_quest_offer_strips_instance_prefix()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_parse_player_id_valid_and_invalid()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_quest_events_no_op_without_dependencies()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_quest_events_registers_handlers()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **UUID** (2 connections)
- **Move followers when the followed player moves.** (1 connections) — `server/game/follow_service.py`
- **Quest event subscriptions: room entry (trigger start), room exit…** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for NPCDied that records kill for kill_N goals when…** (1 connections) — `server/game/quest/quest_events.py`
- *... and 16 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (13 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (7 shared connections)
- [Test Lifespan Event Subscriptions](Test_Lifespan_Event_Subscriptions.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Follow Service](Test_Follow_Service.md) (1 shared connections)
- [Test Quest Service](Test_Quest_Service.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/game/quest/quest_events.py`
- `server/tests/unit/game/test_quest_events.py`

## Audit Trail

- EXTRACTED: 75 (84%)
- INFERRED: 14 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*