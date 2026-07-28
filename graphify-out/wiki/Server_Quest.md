# Server Quest

> 75 nodes

## Key Concepts

- **QuestService** (51 connections) — `server/game/quest/quest_service.py`
- **Any** (27 connections)
- **UUID** (26 connections)
- **QuestDefinitionSchema** (18 connections) — `server/schemas/quest/quest.py`
- **_parse_definition()** (13 connections) — `server/game/quest/quest_service.py`
- **.turn_in()** (12 connections) — `server/game/quest/quest_service.py`
- **._apply_activity_progress()** (11 connections) — `server/game/quest/quest_service.py`
- **._sync_collect_for_instance()** (11 connections) — `server/game/quest/quest_service.py`
- **._complete_instance()** (10 connections) — `server/game/quest/quest_service.py`
- **._turn_in_validation_error()** (10 connections) — `server/game/quest/quest_service.py`
- **._start_quest_validation_error()** (9 connections) — `server/game/quest/quest_service.py`
- **.start_quest()** (9 connections) — `server/game/quest/quest_service.py`
- **.sync_collect_progress()** (9 connections) — `server/game/quest/quest_service.py`
- **._consume_collect_n_items()** (9 connections) — `server/game/quest/quest_service.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_service.py`
- **_goals_met()** (7 connections) — `server/game/quest/quest_service.py`
- **_consume_collect_goals_from_player()** (7 connections) — `server/game/quest/quest_service.py`
- **_build_collect_n_progress()** (7 connections) — `server/game/quest/quest_service.py`
- **._check_prerequisites()** (7 connections) — `server/game/quest/quest_service.py`
- **_has_collect_n_goals()** (6 connections) — `server/game/quest/quest_service.py`
- **.start_quest_by_trigger()** (6 connections) — `server/game/quest/quest_service.py`
- **._load_player_for_collect()** (6 connections) — `server/game/quest/quest_service.py`
- **._apply_item_reward()** (6 connections) — `server/game/quest/quest_service.py`
- **._turn_in_inventory_full_error()** (6 connections) — `server/game/quest/quest_service.py`
- **.turn_in_at_entity()** (6 connections) — `server/game/quest/quest_service.py`
- *... and 50 more nodes in this community*

## Relationships

- [Server Game (44)](Server_Game_%2844%29.md) (19 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (5 shared connections)
- [Server Game (28)](Server_Game_%2828%29.md) (4 shared connections)
- [Server Game (23)](Server_Game_%2823%29.md) (3 shared connections)
- [Server Persistence](Server_Persistence.md) (3 shared connections)
- [Server Game (15)](Server_Game_%2815%29.md) (3 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (2 shared connections)
- [Server Commands (18)](Server_Commands_%2818%29.md) (2 shared connections)
- [Server Events](Server_Events.md) (2 shared connections)
- [Server Container](Server_Container.md) (1 shared connections)
- [Server Commands (2)](Server_Commands_%282%29.md) (1 shared connections)
- [Server Realtime (82)](Server_Realtime_%2882%29.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_service.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 392 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*