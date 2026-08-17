# server services corpse lifecycle service

> 14 nodes

## Key Concepts

- **CorpseServiceError** (11 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_delete_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_not_found_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_persistence_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_not_found()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_service_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Base exception for corpse service operations.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Raised when a corpse container is not found.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Test create_corpse_on_death() handles persistence errors.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test cleanup_decayed_corpse() raises error when delete fails.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test CorpseServiceError exception.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test CorpseNotFoundError exception.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test create_corpse_on_death() raises error when player not found.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (12 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 21 (72%)
- INFERRED: 8 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*