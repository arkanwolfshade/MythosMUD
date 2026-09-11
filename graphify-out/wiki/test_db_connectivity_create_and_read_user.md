# test_db_connectivity_create_and_read_user

> 8 nodes

## Key Concepts

- **test_db_connectivity_create_and_read_user()** (7 connections) — `server/tests/integration/test_db_connectivity.py`
- **cleanup_test_user()** (6 connections) — `server/tests/integration/test_db_connectivity.py`
- **async_sessionmaker** (2 connections)
- **AsyncSession** (2 connections)
- **asyncio** (1 connections)
- **fixture** (1 connections)
- **Yield a fresh user id and guarantee its row is deleted after the test, pass or…** (1 connections) — `server/tests/integration/test_db_connectivity.py`
- **Test that we can create and read a User from the database.** (1 connections) — `server/tests/integration/test_db_connectivity.py`

## Relationships

- [User](User.md) (3 shared connections)
- [session_factory](session_factory.md) (2 shared connections)

## Source Files

- `server/tests/integration/test_db_connectivity.py`

## Audit Trail

- EXTRACTED: 10 (77%)
- INFERRED: 3 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*