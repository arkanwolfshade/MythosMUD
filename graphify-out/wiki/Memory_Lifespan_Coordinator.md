# Memory Lifespan Coordinator

> 11 nodes

## Key Concepts

- **memory_cleanup_service.py** (12 connections) — `server/app/memory_cleanup_service.py`
- **memory_lifespan_coordinator.py** (12 connections) — `server/app/memory_lifespan_coordinator.py`
- **create_memory_cleanup_monitor()** (8 connections) — `server/app/memory_cleanup_service.py`
- **test_create_memory_cleanup_monitor()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **.__init__()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **Managed Task Cleanup Service - Runtime Detection for Memory Threshold…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Create an instance of the MemoryThresholdMonitor with user-specified…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Memory Lifespan Coordinator - Centralized Periodic Auditing for Orphaned Task…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **# TODO: Improve graceful shutdown with early cancellation # pylint:…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Initialize the periodic orphan auditor. Args: check_interval_seconds: Seconds…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Factory returns a configured monitor.** (1 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (9 shared connections)
- [Test Memory Cleanup Service](Test_Memory_Cleanup_Service.md) (8 shared connections)
- [Test Memory Lifespan Coordinator](Test_Memory_Lifespan_Coordinator.md) (4 shared connections)
- [Memory Cleanup Service](Memory_Cleanup_Service.md) (2 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/tests/unit/app/test_memory_cleanup_service.py`

## Audit Trail

- EXTRACTED: 33 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*