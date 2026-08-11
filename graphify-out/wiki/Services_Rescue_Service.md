# Services Rescue Service

> 6 nodes

## Key Concepts

- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **Validate a NATS subject against registered patterns.          Args:** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Record validation metrics if metrics are enabled.          Args:             res** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Cache validation result if caching is enabled.          Args:             subjec** (1 connections) — `server/services/nats_subject_manager/manager.py`

## Relationships

- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (3 shared connections)

## Source Files

- `server/services/nats_subject_manager/manager.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*