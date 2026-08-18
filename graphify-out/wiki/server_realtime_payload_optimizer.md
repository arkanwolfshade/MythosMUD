# server realtime payload optimizer

> 37 nodes

## Key Concepts

- **PayloadOptimizer** (22 connections) — `server/realtime/payload_optimizer.py`
- **test_payload_optimizer.py** (20 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **get_payload_optimizer()** (9 connections) — `server/realtime/payload_optimizer.py`
- **payload_optimizer.py** (6 connections) — `server/realtime/payload_optimizer.py`
- **.optimize_payload()** (5 connections) — `server/realtime/payload_optimizer.py`
- **.compress_payload()** (4 connections) — `server/realtime/payload_optimizer.py`
- **.get_payload_size()** (4 connections) — `server/realtime/payload_optimizer.py`
- **optimizer()** (4 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **Any** (4 connections)
- **_CompareExplodes** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **.create_incremental_update()** (3 connections) — `server/realtime/payload_optimizer.py`
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
- *... and 12 more nodes in this community*

## Relationships

- [server realtime connection helpers](server_realtime_connection_helpers.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server realtime messaging personal message](server_realtime_messaging_personal_message.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [object](object.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/realtime/payload_optimizer.py`
- `server/tests/unit/realtime/test_payload_optimizer.py`

## Audit Trail

- EXTRACTED: 56 (84%)
- INFERRED: 11 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*