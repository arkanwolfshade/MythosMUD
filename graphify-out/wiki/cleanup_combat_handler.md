# cleanup combat handler

> 33 nodes

## Key Concepts

- **test_time_bundle.py** (20 connections) — `server/tests/unit/container/test_time_bundle.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- **_season_for_month()** (5 connections) — `server/time/time_service.py`
- **isolated_chronicle()** (4 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_get_mythos_chronicle_singleton()** (4 connections) — `server/tests/unit/container/test_time_bundle.py`
- **.reset_instance()** (4 connections) — `server/time/time_service.py`
- **test_ensure_utc_naive_datetime()** (3 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_season_for_month()** (3 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_time_bundle_initialize_with_deps()** (2 connections) — `server/tests/unit/container/test_container_bundles.py`
- **test_time_bundle_initialize_missing_deps()** (2 connections) — `server/tests/unit/container/test_container_bundles.py`
- **test_time_bundle_initialize_with_dependencies()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_time_bundle_initialize_missing_dependencies()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_calendar_and_dayparts()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_time_conversion()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_advance_and_freeze()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_format_clock()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_chronicle_advance_rejects_negative_delta()** (2 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Mythos time consumer service.** (1 connections) — `server/container/bundles/time.py`
- **Initialize Mythos time event consumer.** (1 connections) — `server/container/bundles/time.py`
- **test_time_bundle_attrs()** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Unit tests for TimeBundle container wiring.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Naive datetimes are normalized to UTC.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Season mapping follows month bands.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Chronicle with isolated state file.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- *... and 8 more nodes in this community*

## Relationships

- [time service rationale](time_service_rationale.md) (9 shared connections)
- [nats services service](nats_services_service.md) (8 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (2 shared connections)
- [command service commands](command_service_commands.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 93 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*