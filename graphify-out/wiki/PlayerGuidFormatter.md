# PlayerGuidFormatter

> 61 nodes · cohesion 0.05

## Key Concepts

- **PlayerGuidFormatter** (34 connections) — `server/structured_logging/player_guid_formatter.py`
- **test_player_guid_formatter.py** (24 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **_player_service_mock()** (11 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **player_guid_formatter.py** (4 connections) — `server/structured_logging/player_guid_formatter.py`
- **.format()** (4 connections) — `server/structured_logging/player_guid_formatter.py`
- **test_format_guid_at_end()** (4 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_guid_at_start()** (4 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_guid_in_middle()** (4 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_guid_with_hyphens()** (4 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_multiple_guids()** (4 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_player_service_error()** (4 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_with_different_log_levels()** (4 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_with_guid_player_found()** (4 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **._convert_player_guids()** (3 connections) — `server/structured_logging/player_guid_formatter.py`
- **formatter()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_empty_message()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_invalid_guid_format()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_message_with_special_characters()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_no_guids()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_format_with_guid_no_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_player_guid_formatter_init()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_player_guid_formatter_init_with_format()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_uuid_pattern_case_insensitive()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- **test_uuid_pattern_matching()** (3 connections) — `server/tests/unit/structured_logging/test_player_guid_formatter.py`
- *... and 36 more nodes in this community*

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (6 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (1 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/player_guid_formatter.py`
- `server/tests/unit/structured_logging/test_player_guid_formatter.py`

## Audit Trail

- EXTRACTED: 186 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*