# run_quality_fragmentation_guard.py

> 28 nodes

## Key Concepts

- **enhance_player_ids()** (16 connections) — `server/structured_logging/logging_processors.py`
- **set_global_player_service()** (15 connections) — `server/structured_logging/logging_processors.py`
- **test_enhance_player_ids_persistence_error()** (5 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
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
- **test_set_global_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Enhance player_id fields with display names when available.** (1 connections) — `server/structured_logging/logging_processors.py`
- **Set the global player service for logging enhancement. This allows the logging…** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test enhance_player_ids() handles missing player service.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() enhances player_id when player is found.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves player_id unchanged when player not found.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves non-UUID player_id unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves short strings unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles non-string player_id values.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles event_dict without player_id.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles persistence errors gracefully.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles player without name attribute.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 3 more nodes in this community*

## Relationships

- [zone](zone.md) (14 shared connections)
- [required](required.md) (4 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 55 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*