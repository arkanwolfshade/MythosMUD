# enhance player ids()

> 28 nodes

## Key Concepts

- **set_global_player_service()** (17 connections) — `server/structured_logging/logging_processors.py`
- **enhance_player_ids()** (17 connections) — `server/structured_logging/logging_processors.py`
- **test_enhance_player_ids_persistence_error()** (5 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
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
- **Set the global player service for logging enhancement.      This allows the logg** (1 connections) — `server/structured_logging/logging_processors.py`
- **Enhance player_id fields with player names for better log readability.      This** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test set_global_player_service() sets the global player service.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles missing player service.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() enhances player_id when player is found.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves player_id unchanged when player not found.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves non-UUID player_id unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves short strings unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles non-string player_id values.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles event_dict without player_id.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles persistence errors gracefully.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 3 more nodes in this community*

## Relationships

- [QueueListener](QueueListener.md) (14 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [alias storage()](alias_storage%28%29.md) (2 shared connections)
- [.shutdown()](shutdown%28%29.md) (1 shared connections)
- [ASGIApp](ASGIApp.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 94 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*