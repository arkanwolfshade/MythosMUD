# server tests unit utils test

> 67 nodes

## Key Concepts

- **test_error_logging.py** (25 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (24 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception_enhanced()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **log_and_raise_http_enhanced()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception()** (8 connections) — `server/utils/error_logging.py`
- **log_performance_metric()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_websocket()** (7 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (7 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (7 connections) — `server/utils/error_logging.py`
- **log_and_raise_http()** (6 connections) — `server/utils/error_logging.py`
- **Any** (5 connections)
- **test_log_and_raise_enhanced()** (4 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_log_and_raise_enhanced_with_metadata()** (4 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_wrap_third_party_exception_enhanced()** (3 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_create_error_context()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_error_context_with_metadata()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_error_context_to_dict()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_log_and_raise_delegates_to_enhanced()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_wrap_third_party_exception_delegates()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- *... and 42 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (36 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (12 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (5 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (4 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (2 shared connections)
- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 153 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*