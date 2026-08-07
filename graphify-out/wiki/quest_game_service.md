# quest game service

> 124 nodes

## Key Concepts

- **QuestService** (84 connections) — `server/game/quest/quest_service.py`
- **quest_service.py** (32 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (13 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (13 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (13 connections) — `server/game/quest/quest_service.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **._complete_instance()** (11 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **.start_quest()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **._apply_item_reward()** (8 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- *... and 99 more nodes in this community*

## Relationships

- [quest service game](quest_service_game.md) (36 shared connections)
- [quest chat game](quest_chat_game.md) (16 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (11 shared connections)
- [player helpers error](player_helpers_error.md) (9 shared connections)
- [collect inventory game](collect_inventory_game.md) (7 shared connections)
- [collect quest service](collect_quest_service.md) (5 shared connections)
- [spawn npc services](spawn_npc_services.md) (3 shared connections)
- [envelope event game](envelope_event_game.md) (3 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/quest/__init__.py`
- `server/game/quest/quest_chat_notify.py`
- `server/game/quest/quest_service.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 624 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*