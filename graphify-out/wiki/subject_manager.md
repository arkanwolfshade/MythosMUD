# subject_manager

> 7 nodes

## Key Concepts

- **subject_manager()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_cache()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_metrics()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **fixture** (3 connections)
- **Create NATSSubjectManager instance.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Create NATSSubjectManager without metrics.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Create NATSSubjectManager without cache.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Relationships

- [test_manager.py](test_manager.py.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 9 (60%)
- INFERRED: 6 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*