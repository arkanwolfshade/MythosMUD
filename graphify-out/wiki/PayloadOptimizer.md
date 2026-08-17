# PayloadOptimizer

> 28 nodes

## Key Concepts

- **PayloadOptimizer** (22 connections) — `server/realtime/payload_optimizer.py`
- **test_payload_optimizer.py** (20 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **get_payload_optimizer()** (9 connections) — `server/realtime/payload_optimizer.py`
- **payload_optimizer.py** (6 connections) — `server/realtime/payload_optimizer.py`
- **optimizer()** (4 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **_CompareExplodes** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_fallback_on_error()** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_get_payload_size_returns_zero_on_serialization_error()** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
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
- **test_optimize_payload_returns_small_payload_unchanged()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **.__eq__()** (1 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **fixture** (1 connections)
- **Payload optimization for WebSocket messages. This module provides utilities for…** (1 connections) — `server/realtime/payload_optimizer.py`
- **Optimizes payloads for WebSocket transmission. Features: - Size limit…** (1 connections) — `server/realtime/payload_optimizer.py`
- **Get the global payload optimizer instance.** (1 connections) — `server/realtime/payload_optimizer.py`
- *... and 3 more nodes in this community*

## Relationships

- [.optimize_payload](optimize_payload.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (2 shared connections)
- [.send_message](send_message.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/payload_optimizer.py`
- `server/tests/unit/realtime/test_payload_optimizer.py`

## Audit Trail

- EXTRACTED: 43 (75%)
- INFERRED: 14 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*