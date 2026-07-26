# test_logging_processors.py

> 79 nodes · cohesion 0.04

## Key Concepts

- **test_logging_processors.py** (36 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **enhance_player_ids()** (17 connections) — `server/structured_logging/logging_processors.py`
- **set_global_player_service()** (17 connections) — `server/structured_logging/logging_processors.py`
- **sanitize_sensitive_data()** (14 connections) — `server/structured_logging/logging_processors.py`
- **logging_processors.py** (12 connections) — `server/structured_logging/logging_processors.py`
- **configure_enhanced_structlog()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
- **add_request_context()** (11 connections) — `server/structured_logging/logging_processors.py`
- **add_correlation_id()** (8 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (5 connections)
- **test_enhance_player_ids_persistence_error()** (5 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **_EnhancePlayerIdsTls** (4 connections) — `server/structured_logging/logging_processors.py`
- **test_enhance_player_ids_invalid_uuid_format()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_persistence_attribute()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_player_id_field()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_player_service()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_non_string_value()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_found()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_no_name_attribute()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_not_found()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_prevents_recursion()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_short_string()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_correlation_id_existing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_correlation_id_missing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_request_context_adds_logger_name()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_request_context_adds_request_id()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 54 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (2 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 261 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*