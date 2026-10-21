# item_catalog_repository.py

> 62 nodes · cohesion 0.07

## Key Concepts

- **QuestService** (76 connections) — `server/game/quest/quest_service.py`
- **Any** (22 connections)
- **QuestDefinitionSchema** (21 connections) — `server/schemas/quest/quest.py`
- **UUID** (20 connections)
- **_parse_definition()** (13 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (13 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (13 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (11 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (10 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (10 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **.abandon()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **.turn_in_at_entity()** (6 connections) — `server/game/quest/quest_service.py`
- **_definition_completion_mode_error()** (5 connections) — `server/game/quest/quest_service.py`
- **.get_quest_log()** (5 connections) — `server/game/quest/quest_service.py`
- **.record_complete_activity()** (5 connections) — `server/game/quest/quest_service.py`
- **.record_kill()** (5 connections) — `server/game/quest/quest_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (30 shared connections)
- [properties](properties.md) (17 shared connections)
- [endpoints.py](endpoints.py.md) (9 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (8 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (7 shared connections)
- [test_time_bundle.py](test_time_bundle.py.md) (4 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (3 shared connections)
- [mcp.json](mcp.json.md) (3 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [SpellLearningService](SpellLearningService.md) (2 shared connections)

## Source Files

- `server/game/quest/quest_service.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 199 (87%)
- INFERRED: 31 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*