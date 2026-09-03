# Quest Service

> 81 nodes

## Key Concepts

- **QuestService** (77 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestInstance** (21 connections) — `server/models/quest.py`
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
- *... and 56 more nodes in this community*

## Relationships

- [Test Quest Service](Test_Quest_Service.md) (30 shared connections)
- [Collect Inventory](Collect_Inventory.md) (19 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (8 shared connections)
- [Test Chat Npc System](Test_Chat_Npc_System.md) (7 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (6 shared connections)
- [Test Quest Service Collect](Test_Quest_Service_Collect.md) (4 shared connections)
- [Test Lifespan Event Subscriptions](Test_Lifespan_Event_Subscriptions.md) (3 shared connections)
- [Quest Commands](Quest_Commands.md) (3 shared connections)
- [Quest](Quest.md) (3 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/quest/quest_service.py`
- `server/models/quest.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 238 (87%)
- INFERRED: 36 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*