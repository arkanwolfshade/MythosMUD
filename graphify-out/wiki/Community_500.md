# Community 500

> 35 nodes

## Key Concepts

- **RealtimeBundle** (21 connections) — `server/container/bundles/realtime.py`
- **test_realtime_bundle_nats.py** (10 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **._setup_nats_dependent_services()** (7 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_error()** (5 connections) — `server/container/bundles/realtime.py`
- **_config()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_e2e_raises_on_timeout()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_e2e_raises_when_connect_returns_false()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_local_continues_without_nats_on_timeout()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **._handle_nats_connect_false()** (4 connections) — `server/container/bundles/realtime.py`
- **._raise_if_e2e_nats_required()** (4 connections) — `server/container/bundles/realtime.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/realtime.py`
- **test_handle_nats_unavailable_unit_test_soft()** (4 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **asyncio** (4 connections)
- **.shutdown()** (3 connections) — `server/container/bundles/realtime.py`
- **test_handle_nats_unavailable_e2e_raises()** (3 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **Any** (2 connections)
- **BaseException** (1 connections)
- **Any** (1 connections)
- **Attach event publisher and message handler when NATS is available.** (1 connections) — `server/container/bundles/realtime.py`
- **Initialize real-time services. Requires CoreBundle attributes on container.** (1 connections) — `server/container/bundles/realtime.py`
- **Shutdown NATS-related services.** (1 connections) — `server/container/bundles/realtime.py`
- **Real-time communication: NATS, connection manager, event handler.** (1 connections) — `server/container/bundles/realtime.py`
- **Raise if any core dependency is missing.** (1 connections) — `server/container/bundles/realtime.py`
- *... and 10 more nodes in this community*

## Relationships

- [Magic Service Lifespan](Magic_Service_Lifespan.md) (4 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 88](Community_88.md) (3 shared connections)
- [NATS Service Config](NATS_Service_Config.md) (2 shared connections)
- [Community 228](Community_228.md) (2 shared connections)
- [Community 805](Community_805.md) (2 shared connections)
- [Community 106](Community_106.md) (2 shared connections)
- [Community 244](Community_244.md) (2 shared connections)
- [Community 110](Community_110.md) (1 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`

## Audit Trail

- EXTRACTED: 61 (85%)
- INFERRED: 11 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*