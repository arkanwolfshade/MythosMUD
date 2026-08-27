# P4 · Intent Sweep — Core Feature Issues

> 16 nodes

## Key Concepts

- **pylint.py** (9 connections) — `scripts/pylint.py`
- **_CompletedProcessLike** (8 connections) — `scripts/pylint.py`
- **main()** (7 connections) — `scripts/pylint.py`
- **is_pylint_startup_failure()** (5 connections) — `scripts/pylint.py`
- **_report_pylint_failure()** (4 connections) — `scripts/pylint.py`
- **_write_pylint_output()** (4 connections) — `scripts/pylint.py`
- **_combined_output()** (3 connections) — `scripts/pylint.py`
- **_require_pylint_runnable()** (3 connections) — `scripts/pylint.py`
- **_resolve_pylint_cmd()** (3 connections) — `scripts/pylint.py`
- **Path** (3 connections)
- **.stderr()** (1 connections) — `scripts/pylint.py`
- **.stdout()** (1 connections) — `scripts/pylint.py`
- **Protocol** (1 connections)
- **Prefer current interpreter -m pylint (works under uv run --no-sync).** (1 connections) — `scripts/pylint.py`
- **Fail fast before scanning if pylint cannot start (missing package, broken venv).** (1 connections) — `scripts/pylint.py`
- **True when pylint never ran as a linter (missing module, usage/invocation…** (1 connections) — `scripts/pylint.py`

## Relationships

- [test_nats_service_health.py](test_nats_service_health.py.md) (1 shared connections)

## Source Files

- `scripts/pylint.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*