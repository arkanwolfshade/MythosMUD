# server api character creation rationale

> 19 nodes

## Key Concepts

- **test_character_creation.py** (24 connections) — `server/tests/unit/api/test_character_creation.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **TestValidateCharacterStats** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **fixture** (5 connections)
- **.test_validate_stats_invalid_input()** (4 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_validate_stats_with_class()** (4 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_validate_stats_without_class()** (4 connections) — `server/tests/unit/api/test_character_creation.py`
- **mock_profession_service()** (3 connections) — `server/tests/unit/api/test_character_creation.py`
- **mock_request()** (3 connections) — `server/tests/unit/api/test_character_creation.py`
- **mock_stats()** (3 connections) — `server/tests/unit/api/test_character_creation.py`
- **mock_stats_generator()** (3 connections) — `server/tests/unit/api/test_character_creation.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test validate_character_stats() endpoint.** (2 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test validate_character_stats() with class_name.** (2 connections) — `server/tests/unit/api/test_character_creation.py`
- **Validate character stats against class prerequisites. This endpoint checks if…** (1 connections) — `server/api/character_creation.py`
- **Unit tests for character creation API endpoints. Tests roll stats, create…** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Create a mock stats generator.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Create a mock profession service.** (1 connections) — `server/tests/unit/api/test_character_creation.py`

## Relationships

- [server api character creation](server_api_character_creation.md) (15 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (5 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (3 shared connections)
- [computed field](computed_field.md) (3 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (1 shared connections)
- [leveluphook](leveluphook.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (1 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 57 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*