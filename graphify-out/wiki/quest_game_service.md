# quest game service

> 87 nodes

## Key Concepts

- **QuestService** (84 connections) — `server/game/quest/quest_service.py`
- **quest_service.py** (32 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (13 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (13 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (13 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (11 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (8 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._turn_in_inventory_full_error()** (7 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- *... and 62 more nodes in this community*

## Relationships

- [quest service game](quest_service_game.md) (37 shared connections)
- [quest chat game](quest_chat_game.md) (13 shared connections)
- [Database Config](Database_Config.md) (11 shared connections)
- [collect inventory game](collect_inventory_game.md) (7 shared connections)
- [collect quest service](collect_quest_service.md) (5 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (3 shared connections)
- [room sync service](room_sync_service.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)

## Source Files

- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 483 (98%)
- INFERRED: 12 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*