# admin shutdown commands

> 6 nodes

## Key Concepts

- **isolated_chronicle()** (4 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_get_mythos_chronicle_singleton()** (4 connections) — `server/tests/unit/container/test_time_bundle.py`
- **.reset_instance()** (4 connections) — `server/time/time_service.py`
- **Chronicle with isolated state file.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **get_mythos_chronicle returns the same instance.** (1 connections) — `server/tests/unit/container/test_time_bundle.py`
- **Reset the singleton instance (testing support).** (1 connections) — `server/time/time_service.py`

## Relationships

- [player respawn event](player_respawn_event.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (1 shared connections)

## Source Files

- `server/tests/unit/container/test_time_bundle.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*