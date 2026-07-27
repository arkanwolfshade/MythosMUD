# Logging Structured Processors

> 26 nodes · cohesion 0.11

## Key Concepts

- **test_logging_processors.py** (35 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **enhance_player_ids()** (16 connections) — `server/structured_logging/logging_processors.py`
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
- **Enhance player_id fields with player names for better log readability.      This** (1 connections) — `server/structured_logging/logging_processors.py`
- **Unit tests for logging processors.  Tests the logging processors for sanitizing** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles missing player service.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() enhances player_id when player is found.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves player_id unchanged when player not found.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves non-UUID player_id unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() leaves short strings unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles non-string player_id values.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles event_dict without player_id.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles persistence errors gracefully.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() handles player without name attribute.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test enhance_player_ids() prevents recursion.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 1 more nodes in this community*

## Relationships

- [[Logging Structured Processors]] (23 shared connections)
- [[NPC Admin API]] (13 shared connections)
- [[Services Service Room]] (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 108 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
