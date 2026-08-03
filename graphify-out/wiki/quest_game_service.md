# quest game service

> 96 nodes

## Key Concepts

- **QuestService** (84 connections) — `server/game/quest/quest_service.py`
- **quest_service.py** (32 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
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
- *... and 71 more nodes in this community*

## Relationships

- [quest service game](quest_service_game.md) (36 shared connections)
- [quest chat game](quest_chat_game.md) (13 shared connections)
- [Database Config](Database_Config.md) (11 shared connections)
- [collect inventory game](collect_inventory_game.md) (7 shared connections)
- [command parser rationale](command_parser_rationale.md) (5 shared connections)
- [collect quest service](collect_quest_service.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (3 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 507 (96%)
- INFERRED: 19 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*