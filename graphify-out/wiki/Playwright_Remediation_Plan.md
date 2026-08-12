# Playwright Remediation Plan

> 101 nodes

## Key Concepts

- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **create_enhanced_error_context()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **player_state_service.py** (10 connections) — `server/game/player_state_service.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (9 connections) — `server/game/player_creation_service.py`
- **Any** (9 connections)
- **log_structured_error()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **.create_player()** (8 connections) — `server/game/player_creation_service.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **.respawn_player_from_delirium_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **test_enhanced_error_logging.py** (7 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **create_logged_http_exception_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **.respawn_player_by_user_id()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **.apply_lucidity_loss()** (6 connections) — `server/game/player_state_service.py`
- **.apply_fear()** (6 connections) — `server/game/player_state_service.py`
- **.apply_corruption()** (6 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (6 connections) — `server/game/player_state_service.py`
- **.heal_player()** (6 connections) — `server/game/player_state_service.py`
- *... and 76 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (34 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (19 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (17 shared connections)
- [Client Event Store](Client_Event_Store.md) (14 shared connections)
- [Base Command Models](Base_Command_Models.md) (10 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (10 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (8 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (8 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (7 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (6 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (6 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories_inventory.py`
- `server/utils/command_parser.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 448 (95%)
- INFERRED: 22 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*