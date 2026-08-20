# test_realtime_bundle_nats.py

> 15 nodes

## Key Concepts

- **test_realtime_bundle_nats.py** (11 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **_config()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_e2e_raises_on_timeout()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_e2e_raises_when_connect_returns_false()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_local_continues_without_nats_on_timeout()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_handle_nats_unavailable_unit_test_soft()** (4 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **asyncio** (4 connections)
- **test_handle_nats_unavailable_e2e_raises()** (3 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **Any** (1 connections)
- **RealtimeBundle NATS connect policy: e2e hard-fails; soft fail only for non-e2e.** (1 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **e2e_test must not soft-mock missing NATS (avoids silent chat failures in…** (1 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **e2e_test hard-fails when NATS connect times out (e.g. TLS mismatch).** (1 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **Non-e2e local may soft-continue without NATS when connect fails.** (1 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **unit_test combat path still soft-mocks unavailable NATS.** (1 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **e2e_test combat path raises when NATS is unavailable (is_testing=False).** (1 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/container/test_realtime_bundle_nats.py`

## Audit Trail

- EXTRACTED: 25 (86%)
- INFERRED: 4 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*