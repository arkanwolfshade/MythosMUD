# PlayerEnteredRoom

> 137 nodes

## Key Concepts

- **PlayerEnteredRoom** (87 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (51 connections) — `server/events/event_types.py`
- **test_player_event_handlers.py** (32 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_quest_events.py** (16 connections) — `server/tests/unit/game/test_quest_events.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **asyncio** (15 connections)
- **test_player_event_handlers_room_left.py** (15 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **asyncio** (11 connections)
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **fixture** (8 connections)
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (6 connections) — `server/game/quest/quest_events.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- **test_npc_died_no_killer_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_invalid_player_id_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_starts_quest_by_room_trigger()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_left_records_exit_activity()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **asyncio** (5 connections)
- **._on_player_entered_room()** (4 connections) — `server/game/follow_service.py`
- **_entity_id_for_quest_offer()** (4 connections) — `server/game/quest/quest_events.py`
- **_parse_player_id()** (4 connections) — `server/game/quest/quest_events.py`
- **._handle_player_left_room()** (4 connections) — `server/npc/population_control.py`
- **._update_player_count()** (4 connections) — `server/npc/population_control.py`
- *... and 112 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (34 shared connections)
- [NPCBase](NPCBase.md) (21 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (10 shared connections)
- [PlayerEventHandler](PlayerEventHandler.md) (10 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (8 shared connections)
- [FollowService](FollowService.md) (6 shared connections)
- [CorruptionTier](CorruptionTier.md) (5 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [test_population_control.py](test_population_control.py.md) (4 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/game/quest/quest_events.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`

## Audit Trail

- EXTRACTED: 300 (86%)
- INFERRED: 49 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*