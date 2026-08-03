# logging processors structured

> 81 nodes

## Key Concepts

- **test_logging_processors.py** (36 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **set_global_player_service()** (17 connections) — `server/structured_logging/logging_processors.py`
- **enhance_player_ids()** (17 connections) — `server/structured_logging/logging_processors.py`
- **sanitize_sensitive_data()** (14 connections) — `server/structured_logging/logging_processors.py`
- **logging_processors.py** (12 connections) — `server/structured_logging/logging_processors.py`
- **configure_enhanced_structlog()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
- **add_request_context()** (11 connections) — `server/structured_logging/logging_processors.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **add_correlation_id()** (8 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (5 connections)
- **test_enhance_player_ids_persistence_error()** (5 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **_EnhancePlayerIdsTls** (4 connections) — `server/structured_logging/logging_processors.py`
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
- **test_sanitize_sensitive_data_password()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_token()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 56 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [logging setup structured](logging_setup_structured.md) (2 shared connections)
- [logging structured utilities](logging_structured_utilities.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [player guid formatter](player_guid_formatter.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 269 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*