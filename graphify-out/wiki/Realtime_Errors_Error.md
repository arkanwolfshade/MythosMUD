# Realtime Errors Error

> 85 nodes

## Key Concepts

- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
- **command_factories_exploration.py** (11 connections) — `server/utils/command_factories_exploration.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **command_factories_player_state.py** (11 connections) — `server/utils/command_factories_player_state.py`
- **command_factories_utility.py** (11 connections) — `server/utils/command_factories_utility.py`
- **player_state_service.py** (10 connections) — `server/game/player_state_service.py`
- **wrap_third_party_exception_enhanced()** (10 connections) — `server/utils/enhanced_error_logging.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (9 connections) — `server/game/player_creation_service.py`
- **Any** (9 connections)
- **log_structured_error()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **.create_player()** (8 connections) — `server/game/player_creation_service.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **create_logged_http_exception_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **.respawn_player_by_user_id()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **.update_player_location()** (6 connections) — `server/game/player_service.py`
- **.apply_lucidity_loss()** (6 connections) — `server/game/player_state_service.py`
- *... and 60 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (40 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (23 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (17 shared connections)
- [Base Command Models](Base_Command_Models.md) (14 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (13 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (12 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (11 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (11 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (10 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (6 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (5 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (5 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/structured_logging/logging_context.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_exploration.py`
- `server/utils/command_factories_moderation.py`
- `server/utils/command_factories_player_state.py`
- `server/utils/command_factories_utility.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 457 (93%)
- INFERRED: 32 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*