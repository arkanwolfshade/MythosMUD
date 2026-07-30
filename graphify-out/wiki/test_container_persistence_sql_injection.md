# test container persistence sql injection

> 8 nodes

## Key Concepts

- **TestCreateErrorContext** (12 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_create_error_context_with_user()** (3 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_create_error_context_no_user()** (3 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_create_error_context_no_request()** (3 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test create_error_context function.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test create_error_context includes user information (returns flat dict for **kwa** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test create_error_context handles None user (returns flat dict).** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test create_error_context handles None request (returns flat dict).** (1 connections) — `server/tests/unit/api/test_container_helpers.py`

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (5 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [metrics](metrics.md) (1 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_container_helpers.py`

## Audit Trail

- EXTRACTED: 18 (72%)
- INFERRED: 7 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*