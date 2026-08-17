# test_quest_events.py

> 39 nodes

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
- **_entity_id_for_quest_offer()** (4 connections) — `server/game/quest/quest_events.py`
- **_parse_player_id()** (4 connections) — `server/game/quest/quest_events.py`
- **Any** (4 connections)
- **test_entity_id_for_quest_offer_plain_room_unchanged()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_entity_id_for_quest_offer_strips_instance_prefix()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_parse_player_id_valid_and_invalid()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_quest_events_no_op_without_dependencies()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_quest_events_registers_handlers()** (3 connections) — `server/tests/unit/game/test_quest_events.py`
- **UUID** (2 connections)
- **Quest event subscriptions: room entry (trigger start), room exit…** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for NPCDied that records kill for kill_N goals when…** (1 connections) — `server/game/quest/quest_events.py`
- **Parse player_id string to UUID. Returns None if invalid.** (1 connections) — `server/game/quest/quest_events.py`
- **Return entity_id for quest_offers lookup: strip instance_<uuid>_ prefix if…** (1 connections) — `server/game/quest/quest_events.py`
- *... and 14 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (13 shared connections)
- [NPCDied](NPCDied.md) (6 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [FollowService](FollowService.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_events.py`
- `server/tests/unit/game/test_quest_events.py`

## Audit Trail

- EXTRACTED: 72 (84%)
- INFERRED: 14 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*