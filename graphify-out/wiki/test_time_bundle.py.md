# test_time_bundle.py

> 33 nodes

## Key Concepts

- **test_time_bundle.py** (21 connections) — `server/tests/unit/container/test_time_bundle.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
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
- **Mythos time consumer service.** (1 connections) — `server/container/bundles/time.py`
- **Initialize Mythos time event consumer.** (1 connections) — `server/container/bundles/time.py`
- **Unit tests for TimeBundle container wiring.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Advance and freeze update persisted state.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Clock formatting includes Mythos suffix.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **get_mythos_chronicle returns the same instance.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- *... and 8 more nodes in this community*

## Relationships

- [MythosTickScheduler](MythosTickScheduler.md) (7 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [HolidayService](HolidayService.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 54 (87%)
- INFERRED: 8 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*