# test_time_bundle.py

> 29 nodes

## Key Concepts

- **test_time_bundle.py** (21 connections) — `server/tests/unit/container/test_time_bundle.py`
- **isolated_chronicle()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_get_mythos_chronicle_singleton()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **_season_for_month()** (5 connections) — `server/time/time_service.py`
- **.reset_instance()** (4 connections) — `server/time/time_service.py`
- **test_ensure_utc_naive_datetime()** (3 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_season_for_month()** (3 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_time_bundle_initialize_missing_dependencies()** (3 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_time_bundle_initialize_with_dependencies()** (3 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_advance_and_freeze()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_advance_rejects_negative_delta()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_calendar_and_dayparts()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_format_clock()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_time_conversion()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **asyncio** (2 connections)
- **test_time_bundle_attrs()** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **fixture** (1 connections)
- **Unit tests for TimeBundle container wiring.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Advance and freeze update persisted state.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Clock formatting includes Mythos suffix.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **get_mythos_chronicle returns the same instance.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **advance_mythos rejects negative hours.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Naive datetimes are normalized to UTC.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Season mapping follows month bands.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Chronicle with isolated state file.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- *... and 4 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (4 shared connections)
- [datetime](datetime.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/container/test_time_bundle.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 43 (91%)
- INFERRED: 4 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*