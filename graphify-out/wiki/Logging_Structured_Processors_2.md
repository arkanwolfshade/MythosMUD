# Logging Structured Processors

> 30 nodes

## Key Concepts

- **enhance_player_ids()** (18 connections) — `server/structured_logging/logging_processors.py`
- **set_global_player_service()** (17 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (6 connections)
- **test_enhance_player_ids_persistence_error()** (5 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **_enhance_one_player_id()** (4 connections) — `server/structured_logging/logging_processors.py`
- **test_enhance_player_ids_no_player_service()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_found()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_not_found()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_invalid_uuid_format()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_short_string()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_non_string_value()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_player_id_field()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_no_name_attribute()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_prevents_recursion()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_persistence_attribute()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_set_global_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Set the global player service for logging enhancement.      This allows the lo** (1 connections) — `server/structured_logging/logging_processors.py`
- **Enhance player_id fields with display names when available.** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test set_global_player_service() sets the global player service.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles missing player service.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() enhances player_id when player is found.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves player_id unchanged when player not found.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves non-UUID player_id unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves short strings unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles non-string player_id values.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 5 more nodes in this community*

## Relationships

- [Test Refactoring Deliverables](Test_Refactoring_Deliverables.md) (15 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Archive Bug Prevention](Archive_Bug_Prevention.md) (4 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Archive Planning Aliases](Archive_Planning_Aliases.md) (1 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 104 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*