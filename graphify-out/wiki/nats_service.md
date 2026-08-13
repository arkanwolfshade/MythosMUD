# nats_service

> 5 nodes

## Key Concepts

- **nats_service()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **fixture** (2 connections)
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Create a NATSService instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [test_nats_service.py](test_nats_service.py.md) (2 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 8 (80%)
- INFERRED: 2 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*