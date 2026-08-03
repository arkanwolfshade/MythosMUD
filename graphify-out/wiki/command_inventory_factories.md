# command inventory factories

> 165 nodes

## Key Concepts

- **exceptions.py** (238 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **error_logging.py** (56 connections) — `server/utils/error_logging.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **WearableContainerServiceError** (22 connections) — `server/services/wearable_container_service.py`
- **test_enhanced_error_logging.py** (22 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **professions.py** (19 connections) — `server/api/professions.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **environmental_container_loader.py** (14 connections) — `server/services/environmental_container_loader.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **command_factories_utility.py** (11 connections) — `server/utils/command_factories_utility.py`
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **get_all_professions()** (10 connections) — `server/api/professions.py`
- **get_profession_by_id()** (10 connections) — `server/api/professions.py`
- **player_state_service.py** (10 connections) — `server/game/player_state_service.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- *... and 140 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (49 shared connections)
- [models npc rationale](models_npc_rationale.md) (39 shared connections)
- [Database Config](Database_Config.md) (39 shared connections)
- [command inventory models](command_inventory_models.md) (38 shared connections)
- [Exception Containers](Exception_Containers.md) (31 shared connections)
- [Loot Generation](Loot_Generation.md) (24 shared connections)
- [wearable container service](wearable_container_service.md) (22 shared connections)
- [player service game](player_service_game.md) (18 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (14 shared connections)
- [Inventory Equip](Inventory_Equip.md) (13 shared connections)
- [game chat service](game_chat_service.md) (12 shared connections)
- [admin auth service](admin_auth_service.md) (11 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/api/professions.py`
- `server/exceptions.py`
- `server/game/player_creation_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/environmental_container_loader.py`
- `server/services/wearable_container_service.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/command_factories_utility.py`
- `server/utils/command_parser.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 1055 (95%)
- INFERRED: 53 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*