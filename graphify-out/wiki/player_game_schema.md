# player game schema

> 65 nodes

## Key Concepts

- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (22 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **Any** (9 connections)
- **create_logged_http_exception_enhanced()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **log_and_raise_http_enhanced()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception()** (8 connections) — `server/utils/error_logging.py`
- **log_performance_metric()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_websocket()** (7 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (7 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (7 connections) — `server/utils/error_logging.py`
- **log_and_raise_http()** (6 connections) — `server/utils/error_logging.py`
- **increment_exception()** (5 connections) — `server/monitoring/exception_metrics.py`
- **Any** (5 connections)
- **test_log_and_raise_enhanced()** (4 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_log_and_raise_enhanced_with_metadata()** (4 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_wrap_third_party_exception_enhanced()** (3 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_log_and_raise_delegates_to_enhanced()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_wrap_third_party_exception_delegates()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_error_context()** (2 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- *... and 40 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (28 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (8 shared connections)
- [Inventory Equip](Inventory_Equip.md) (5 shared connections)
- [add used user](add_used_user.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (5 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [admin command setstat](admin_command_setstat.md) (2 shared connections)
- [population npc control](population_npc_control.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_metrics.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 250 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*