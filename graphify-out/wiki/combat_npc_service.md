# combat npc service

> 76 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **StatSummary** (8 connections) — `server/schemas/players/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- **Any** (6 connections)
- **.test_create_character_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **Stats** (5 connections)
- **_validate_user_for_stats_roll()** (5 connections) — `server/api/character_creation.py`
- **_apply_rate_limiting_for_stats_roll()** (5 connections) — `server/api/character_creation.py`
- **_apply_stat_modifiers()** (5 connections) — `server/api/character_creation.py`
- *... and 51 more nodes in this community*

## Relationships

- [commands admin helpers](commands_admin_helpers.md) (24 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (14 shared connections)
- [Player Stats](Player_Stats.md) (11 shared connections)
- [System Metrics](System_Metrics.md) (10 shared connections)
- [player requests schemas](player_requests_schemas.md) (10 shared connections)
- [error websocket handler](error_websocket_handler.md) (7 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (4 shared connections)
- [health realtime monitoring](health_realtime_monitoring.md) (3 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/game/profession_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 358 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*