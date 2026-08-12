# ._connect_nats

> 10 nodes

## Key Concepts

- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_error()** (5 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_false()** (4 connections) — `server/container/bundles/realtime.py`
- **._raise_if_e2e_nats_required()** (4 connections) — `server/container/bundles/realtime.py`
- **Any** (1 connections)
- **BaseException** (1 connections)
- **Raise RuntimeError when e2e requires live NATS; no-op for other environments.** (1 connections) — `server/container/bundles/realtime.py`
- **Convert connect failures into hard error (e2e) or soft log (other envs).** (1 connections) — `server/container/bundles/realtime.py`
- **Handle connect() returning False; raise for e2e, soft-warn otherwise.** (1 connections) — `server/container/bundles/realtime.py`
- **Connect to NATS if enabled and not unit_test. Returns NATSService or None.…** (1 connections) — `server/container/bundles/realtime.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/container/bundles/realtime.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*