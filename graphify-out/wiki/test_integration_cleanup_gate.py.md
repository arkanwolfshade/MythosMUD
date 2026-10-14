# test_integration_cleanup_gate.py

> 14 nodes

## Key Concepts

- **test_integration_cleanup_gate.py** (10 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **_test_touches_database()** (9 connections) — `server/tests/fixtures/integration/__init__.py`
- **_Node** (4 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **test_integration_marked_test_is_cleaned_up()** (4 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **test_plain_unit_test_skips_cleanup()** (4 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **test_unit_test_that_asks_for_session_factory_is_cleaned_up()** (4 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **_plain_unit_test()** (3 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **test_request_without_a_test_function_skips_cleanup()** (3 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **.__init__()** (2 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **_unit_test_using_db()** (2 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **.get_closest_marker()** (1 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **.__init__()** (1 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **True for integration-tier tests and any test that asks for session_factory…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Unit tests for the integration-cleanup gate (#949). The integration fixture…** (1 connections) — `server/tests/unit/test_integration_cleanup_gate.py`

## Relationships

- [PlayerService](PlayerService.md) (4 shared connections)
- [session_factory](session_factory.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/unit/test_integration_cleanup_gate.py`

## Audit Trail

- EXTRACTED: 22 (76%)
- INFERRED: 7 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*