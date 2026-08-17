# server game quest quest service

> 77 nodes

## Key Concepts

- **QuestService** (79 connections) — `server/game/quest/quest_service.py`
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
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (8 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._turn_in_inventory_full_error()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **.turn_in_at_entity()** (6 connections) — `server/game/quest/quest_service.py`
- **_call_add_item_to_inventory()** (5 connections) — `server/game/quest/quest_service.py`
- *... and 52 more nodes in this community*

## Relationships

- [server tests unit game test](server_tests_unit_game_test.md) (34 shared connections)
- [server game quest collect inventory](server_game_quest_collect_inventory.md) (18 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (10 shared connections)
- [server game chat npc system](server_game_chat_npc_system.md) (7 shared connections)
- [server api players get player](server_api_players_get_player.md) (4 shared connections)
- [server commands quest commands](server_commands_quest_commands.md) (3 shared connections)
- [leveluphook](leveluphook.md) (2 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (2 shared connections)
- [server api players](server_api_players.md) (1 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [server game magic spell effect](server_game_magic_spell_effect.md) (1 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_service.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 221 (85%)
- INFERRED: 38 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*