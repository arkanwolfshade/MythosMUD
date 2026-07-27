# Integration DB Fixtures

> 6 nodes · cohesion 0.09

## Key Concepts

- **async_sessionmaker** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **AsyncSession** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **FixtureRequest** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **AsyncSession** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **AsyncEngine** (2 connections) — `server/tests/fixtures/integration/__init__.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/integration/test_procedures_return_shape.py`

## Audit Trail

- EXTRACTED: 19 (70%)
- INFERRED: 8 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*