# QuestCompleted

> 79 nodes

## Key Concepts

- **QuestService** (53 connections) — `server/game/quest/quest_service.py`
- **quest_service.py** (31 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (13 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (12 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (12 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (11 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (7 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (6 connections) — `server/game/quest/quest_service.py`
- **._turn_in_inventory_full_error()** (6 connections) — `server/game/quest/quest_service.py`
- *... and 54 more nodes in this community*

## Relationships

- [bench cache npc](bench_cache_npc.md) (11 shared connections)
- [.initialize()](initialize%28%29.md) (10 shared connections)
- [UUID](UUID.md) (8 shared connections)
- [collect inventory](collect_inventory.md) (6 shared connections)
- [test player event handlers respawn](test_player_event_handlers_respawn.md) (5 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (5 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (3 shared connections)
- [test quest service](test_quest_service.md) (3 shared connections)
- [Calculate max magic points (MP)](Calculate_max_magic_points_%28MP%29.md) (3 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (2 shared connections)

## Source Files

- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 430 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*