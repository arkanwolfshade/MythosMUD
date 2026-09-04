# Test Logging Processors

> 83 nodes

## Key Concepts

- **test_logging_processors.py** (38 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **enhance_player_ids()** (19 connections) — `server/structured_logging/logging_processors.py`
- **set_global_player_service()** (18 connections) — `server/structured_logging/logging_processors.py`
- **sanitize_sensitive_data()** (14 connections) — `server/structured_logging/logging_processors.py`
- **logging_processors.py** (13 connections) — `server/structured_logging/logging_processors.py`
- **add_request_context()** (11 connections) — `server/structured_logging/logging_processors.py`
- **configure_enhanced_structlog()** (10 connections) — `server/structured_logging/enhanced_logging_config.py`
- **add_correlation_id()** (8 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (5 connections)
- **_enhance_one_player_id()** (4 connections) — `server/structured_logging/logging_processors.py`
- **test_enhance_player_ids_invalid_uuid_format()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_persistence_attribute()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_player_id_field()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_player_service()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_non_string_value()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_persistence_error()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_found()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_no_name_attribute()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_not_found()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_prevents_recursion()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_short_string()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_swallows_database_error_without_importing_it()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **_EnhancePlayerIdsTls** (3 connections) — `server/structured_logging/logging_processors.py`
- **mock_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **sample_event_dict()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 58 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (10 shared connections)
- [Test Logging Utilities](Test_Logging_Utilities.md) (2 shared connections)
- [Logging File Setup](Logging_File_Setup.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 148 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*