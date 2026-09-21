# NPCDied

> 82 nodes

## Key Concepts

- **NPCDied** (29 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (29 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **_make_manager()** (19 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **test_quest_events.py** (16 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **_LifecycleManagerForDeath** (12 connections) — `server/npc/lifecycle_death.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_mark_despawned_and_queue_respawn()** (10 connections) — `server/npc/lifecycle_death.py`
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (6 connections) — `server/game/quest/quest_events.py`
- **test_handle_npc_died_impl_full_path()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_mark_despawned_logs_failure()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_npc_died_no_killer_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_invalid_player_id_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_starts_quest_by_room_trigger()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_left_records_exit_activity()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **_manager_stub()** (5 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **asyncio** (5 connections)
- **_entity_id_for_quest_offer()** (4 connections) — `server/game/quest/quest_events.py`
- **_parse_player_id()** (4 connections) — `server/game/quest/quest_events.py`
- *... and 57 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (44 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (7 shared connections)
- [NPCBase](NPCBase.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [._bind_event_type](_bind_event_type.md) (4 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)
- [QuestService](QuestService.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_manager.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 186 (87%)
- INFERRED: 29 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*