# player room event

> 38 nodes

## Key Concepts

- **test_quest_events.py** (16 connections) — `server/tests/unit/game/test_quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_entered()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (6 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (5 connections) — `server/game/quest/quest_events.py`
- **_entity_id_for_quest_offer()** (4 connections) — `server/game/quest/quest_events.py`
- **Any** (4 connections)
- **_parse_player_id()** (4 connections) — `server/game/quest/quest_events.py`
- **test_player_entered_starts_quest_by_room_trigger()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_invalid_player_id_skips()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_left_records_exit_activity()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_no_killer_skips()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_entity_id_for_quest_offer_strips_instance_prefix()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_entity_id_for_quest_offer_plain_room_unchanged()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_parse_player_id_valid_and_invalid()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_quest_events_no_op_without_dependencies()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_quest_events_registers_handlers()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **UUID** (2 connections)
- **Quest event subscriptions: room entry (trigger start), room exit (complete_activ** (1 connections) — `server/game/quest/quest_events.py`
- **Return entity_id for quest_offers lookup: strip instance_<uuid>_ prefix if prese** (1 connections) — `server/game/quest/quest_events.py`
- **Subscribe to room events for quest triggers and progress.      - PlayerEnteredRo** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for PlayerEnteredRoom (entering via exit); starts room-o** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for PlayerLeftRoom that records exit_<room_id> activity.** (1 connections) — `server/game/quest/quest_events.py`
- *... and 13 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [spawn npc services](spawn_npc_services.md) (2 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)
- [party service game](party_service_game.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_events.py`
- `server/tests/unit/game/test_quest_events.py`

## Audit Trail

- EXTRACTED: 125 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*