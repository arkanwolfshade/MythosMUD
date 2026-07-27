# Asyncio Run Guardrails

> 4 nodes · cohesion 0.50

## Key Concepts

- **test_asyncio_run_guardrails.py** (2 connections) — `server/tests/unit/test_asyncio_run_guardrails.py`
- **test_no_asyncio_run_in_server_library_code()** (2 connections) — `server/tests/unit/test_asyncio_run_guardrails.py`
- **Test that server library code does not use asyncio.run() (AnyIO best practice).** (1 connections) — `server/tests/unit/test_asyncio_run_guardrails.py`
- **Assert server/ has no asyncio.run() in library code (use anyio.run() at entry po** (1 connections) — `server/tests/unit/test_asyncio_run_guardrails.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/tests/unit/test_asyncio_run_guardrails.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
