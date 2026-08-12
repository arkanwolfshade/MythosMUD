# Quest Service Core

> 73 nodes

## Key Concepts

- **QuestService** (53 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (12 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (11 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (11 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (6 connections) — `server/game/quest/quest_service.py`
- **._turn_in_inventory_full_error()** (6 connections) — `server/game/quest/quest_service.py`
- **.turn_in_at_entity()** (6 connections) — `server/game/quest/quest_service.py`
- **_call_add_item_to_inventory()** (5 connections) — `server/game/quest/quest_service.py`
- **_definition_completion_mode_error()** (5 connections) — `server/game/quest/quest_service.py`
- *... and 48 more nodes in this community*

## Relationships

- [Async Audit Cursor](Async_Audit_Cursor.md) (18 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (9 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [Whisper Testing Complete](Whisper_Testing_Complete.md) (4 shared connections)
- [Player GUID Formatter](Player_GUID_Formatter.md) (3 shared connections)
- [Command Service Tests](Command_Service_Tests.md) (3 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Lucidity Database Models](Lucidity_Database_Models.md) (2 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [AI Agent Development Docs](AI_Agent_Development_Docs.md) (1 shared connections)
- [Chat Spec Archive](Chat_Spec_Archive.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_service.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 379 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*