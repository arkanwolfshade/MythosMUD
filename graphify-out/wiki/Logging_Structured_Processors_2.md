# Logging Structured Processors

> 82 nodes

## Key Concepts

- **test_logging_processors.py** (36 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **enhance_player_ids()** (18 connections) — `server/structured_logging/logging_processors.py`
- **set_global_player_service()** (17 connections) — `server/structured_logging/logging_processors.py`
- **logging_processors.py** (14 connections) — `server/structured_logging/logging_processors.py`
- **sanitize_sensitive_data()** (14 connections) — `server/structured_logging/logging_processors.py`
- **configure_enhanced_structlog()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
- **add_request_context()** (11 connections) — `server/structured_logging/logging_processors.py`
- **add_correlation_id()** (8 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (6 connections)
- **test_enhance_player_ids_persistence_error()** (5 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **_EnhancePlayerIdsTls** (4 connections) — `server/structured_logging/logging_processors.py`
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
- **_database_error_type()** (3 connections) — `server/structured_logging/logging_processors.py`
- **test_set_global_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_password()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 57 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (9 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Logging Path Utilities](Logging_Path_Utilities.md) (2 shared connections)
- [Logging File Setup](Logging_File_Setup.md) (1 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 273 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*