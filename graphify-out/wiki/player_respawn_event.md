# player respawn event

> 25 nodes

## Key Concepts

- **test_time_bundle.py** (20 connections) — `server/tests/unit/container/test_time_bundle.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- **_season_for_month()** (5 connections) — `server/time/time_service.py`
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
- **Season mapping follows month bands.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Calendar components and daypart helpers.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Real/Mythos datetime conversion round-trips approximately.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Advance and freeze update persisted state.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Clock formatting includes Mythos suffix.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **advance_mythos rejects negative hours.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Return the lore-friendly season label for the provided month number.** (1 connections) — `server/time/time_service.py`

## Relationships

- [nats services service](nats_services_service.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (4 shared connections)
- [time service rationale](time_service_rationale.md) (4 shared connections)
- [command service commands](command_service_commands.md) (2 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (2 shared connections)
- [admin shutdown commands](admin_shutdown_commands.md) (2 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 74 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*