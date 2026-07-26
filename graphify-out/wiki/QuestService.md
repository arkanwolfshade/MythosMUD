# QuestService

> 46 nodes · cohesion 0.06

## Key Concepts

- **QuestService** (53 connections) — `server/game/quest/quest_service.py`
- **Any** (26 connections)
- **UUID** (26 connections)
- **quest_service.py** (25 connections) — `server/game/quest/quest_service.py`
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (12 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (11 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (11 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **QuestCompleted** (9 connections) — `server/events/event_types.py`
- **.start_quest()** (9 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **.turn_in_at_entity()** (6 connections) — `server/game/quest/quest_service.py`
- **_call_add_item_to_inventory()** (5 connections) — `server/game/quest/quest_service.py`
- **_definition_completion_mode_error()** (5 connections) — `server/game/quest/quest_service.py`
- *... and 21 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (10 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [consume_prototype_from_player](consume_prototype_from_player.md) (6 shared connections)
- [exceptions.py](exceptions.py.md) (5 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (4 shared connections)
- [quest_commands.py](quest_commands.py.md) (3 shared connections)
- [__init__.py](__init__.py.md) (2 shared connections)
- [dependencies.py](dependencies.py.md) (2 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/quest/__init__.py`
- `server/game/quest/quest_service.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 369 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*