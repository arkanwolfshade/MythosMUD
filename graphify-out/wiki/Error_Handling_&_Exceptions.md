# Error Handling & Exceptions

> 414 nodes

## Key Concepts

- **server/exceptions.py** (245 connections) — `server/exceptions.py`
- **DatabaseError** (224 connections) — `server/exceptions.py`
- **MythosMUDError** (53 connections) — `server/exceptions.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **test_exceptions.py** (44 connections) — `server/tests/unit/test_exceptions.py`
- **ErrorContext** (40 connections) — `server/exceptions.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **error_types.py** (35 connections) — `server/error_types.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **standardized_responses.py** (34 connections) — `server/error_handlers/standardized_responses.py`
- **ErrorType** (31 connections) — `server/error_types.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **test_command_factories_communication.py** (30 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **create_error_context()** (23 connections) — `server/exceptions.py`
- **test_quest_instance_repository.py** (23 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **create_standard_error_response()** (22 connections) — `server/error_types.py`
- **test_quest_definition_repository.py** (21 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **LoggedException** (20 connections) — `server/exceptions.py`
- **create_websocket_error_response()** (20 connections) — `server/error_types.py`
- **quest_instance_repository.py** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **ErrorMessages** (18 connections) — `server/error_types.py`
- **test_error_types.py** (18 connections) — `server/tests/unit/test_error_types.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- *... and 389 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (43 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (27 shared connections)
- [Pydantic Error Handler](Pydantic_Error_Handler.md) (26 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (26 shared connections)
- [Test Error Logging](Test_Error_Logging.md) (26 shared connections)
- [Test Command Factories Communication](Test_Command_Factories_Communication.md) (26 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (25 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (21 shared connections)
- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (20 shared connections)
- [Player Skill Repository](Player_Skill_Repository.md) (20 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (19 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (13 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `scripts/populate_test_npc_databases.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/models/quest.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/realtime/connection_event_helpers.py`
- `server/services/combat_messaging_service.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 1373 (90%)
- INFERRED: 154 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*