# npc event handlers

> 27 nodes

## Key Concepts

- **PayloadOptimizer** (23 connections) — `server/realtime/payload_optimizer.py`
- **test_payload_optimizer.py** (19 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **get_payload_optimizer()** (9 connections) — `server/realtime/payload_optimizer.py`
- **payload_optimizer.py** (6 connections) — `server/realtime/payload_optimizer.py`
- **_CompareExplodes** (4 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **optimizer()** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_fallback_on_error()** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **.__init__()** (2 connections) — `server/realtime/payload_optimizer.py`
- **test_get_payload_size_returns_byte_length()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_get_payload_size_returns_zero_on_serialization_error()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_compress_payload_round_trip_metadata()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_returns_small_payload_unchanged()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_compresses_large_payload()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_force_compression_when_beneficial()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_raises_when_uncompressible_and_oversized()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_optimize_payload_raises_when_compressed_still_too_large()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_no_previous_returns_full()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_detects_changes()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_create_incremental_update_empty_when_unchanged()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_get_payload_optimizer_returns_singleton()** (2 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **Payload optimization for WebSocket messages.  This module provides utilities for** (1 connections) — `server/realtime/payload_optimizer.py`
- **Optimizes payloads for WebSocket transmission.      Features:     - Size limit e** (1 connections) — `server/realtime/payload_optimizer.py`
- **Initialize the payload optimizer.          Args:             max_payload_size: M** (1 connections) — `server/realtime/payload_optimizer.py`
- **Get the global payload optimizer instance.** (1 connections) — `server/realtime/payload_optimizer.py`
- **.__eq__()** (1 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- *... and 2 more nodes in this community*

## Relationships

- [payload realtime optimizer](payload_realtime_optimizer.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (1 shared connections)
- [startup services npc](startup_services_npc.md) (1 shared connections)

## Source Files

- `server/realtime/payload_optimizer.py`
- `server/tests/unit/realtime/test_payload_optimizer.py`

## Audit Trail

- EXTRACTED: 98 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*