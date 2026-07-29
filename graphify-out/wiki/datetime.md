# datetime

> 13 nodes

## Key Concepts

- **_utc_now()** (8 connections) — `server/models/lucidity.py`
- **test_lucidity_utils.py** (7 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_naive_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_utc_time()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_different_times()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **datetime** (2 connections)
- **Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibi** (1 connections) — `server/models/lucidity.py`
- **Unit tests for lucidity model utility functions.  Tests the _utc_now utility fun** (1 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **Test _utc_now returns a datetime object.** (1 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **Test _utc_now returns naive datetime (tzinfo=None).** (1 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **Test _utc_now returns time close to current UTC time.** (1 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **Test _utc_now returns different times on subsequent calls.** (1 connections) — `server/tests/unit/models/test_lucidity_utils.py`

## Relationships

- [. init ()](_init_%28%29.md) (3 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/tests/unit/models/test_lucidity_utils.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*