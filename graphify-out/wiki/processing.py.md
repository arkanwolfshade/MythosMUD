# processing.py

> 38 nodes · cohesion 0.09

## Key Concepts

- **PayloadOptimizer** (23 connections) — `server/realtime/payload_optimizer.py`
- **test_payload_optimizer.py** (20 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **get_payload_optimizer()** (9 connections) — `server/realtime/payload_optimizer.py`
- **payload_optimizer.py** (6 connections) — `server/realtime/payload_optimizer.py`
- **.optimize_payload()** (6 connections) — `server/realtime/payload_optimizer.py`
- **.compress_payload()** (4 connections) — `server/realtime/payload_optimizer.py`
- **.get_payload_size()** (4 connections) — `server/realtime/payload_optimizer.py`
- **Any** (4 connections)
- **optimizer()** (4 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **.create_incremental_update()** (3 connections) — `server/realtime/payload_optimizer.py`
- **_CompareExplodes** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_fallback_on_error()** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_get_payload_size_measures_non_json_values()** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **.__init__()** (2 connections) — `server/realtime/payload_optimizer.py`
- **test_compress_payload_round_trip_metadata()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_detects_changes()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_empty_when_unchanged()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_no_previous_returns_full()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_get_payload_optimizer_returns_singleton()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_get_payload_size_returns_byte_length()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_compresses_large_payload()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_force_compression_when_beneficial()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_raises_when_compressed_still_too_large()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_raises_when_uncompressible_and_oversized()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_rejects_oversized_payload_with_datetime()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- *... and 13 more nodes in this community*

## Relationships

- [Room](Room.md) (3 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (1 shared connections)

## Source Files

- `server/realtime/payload_optimizer.py`
- `server/tests/unit/realtime/test_payload_optimizer.py`

## Audit Trail

- EXTRACTED: 57 (83%)
- INFERRED: 12 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*