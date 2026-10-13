# Community 397

> 44 nodes

## Key Concepts

- **test_quest_events.py** (14 connections) — `server/tests/unit/game/test_quest_events.py`
- **subscribe_quest_events()** (13 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (12 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_entered()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (6 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (6 connections) — `server/game/quest/quest_events.py`
- **asyncio** (6 connections)
- **._on_player_entered_room()** (4 connections) — `server/game/follow_service.py`
- **_entity_id_for_quest_offer()** (4 connections) — `server/game/quest/quest_events.py`
- **_parse_player_id()** (4 connections) — `server/game/quest/quest_events.py`
- **test_npc_died_no_killer_skips()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_invalid_player_id_skips()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_starts_quest_by_room_trigger()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_left_records_exit_activity()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_left_without_destination_is_not_an_exit()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **Any** (4 connections)
- **test_entity_id_for_quest_offer_plain_room_unchanged()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_entity_id_for_quest_offer_strips_instance_prefix()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_parse_player_id_valid_and_invalid()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_quest_events_no_op_without_dependencies()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_quest_events_registers_handlers()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **UUID** (2 connections)
- **PlayerEnteredRoom** (1 connections)
- **Move followers when the followed player moves.** (1 connections) — `server/game/follow_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [Community 318](Community_318.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Game Event Types](Game_Event_Types.md) (2 shared connections)
- [Community 99](Community_99.md) (1 shared connections)
- [Community 130](Community_130.md) (1 shared connections)
- [Community 1444](Community_1444.md) (1 shared connections)
- [Community 1271](Community_1271.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/game/quest/quest_events.py`
- `server/tests/unit/game/test_quest_events.py`

## Audit Trail

- EXTRACTED: 72 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*