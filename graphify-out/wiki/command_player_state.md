# command player state

> 22 nodes

## Key Concepts

- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **__init__.py** (12 connections) — `server/services/nats_subject_manager/__init__.py`
- **.__init__()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **patterns.py** (3 connections) — `server/services/nats_subject_manager/patterns.py`
- **metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_subject_manager_metrics_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **.record_validation()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_build()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_error()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.reset()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **NATS Subject Manager for MythosMUD.  This package provides centralized subject n** (1 connections) — `server/services/nats_subject_manager/__init__.py`
- **Initialize NATS Subject Manager.          Args:             enable_cache: Enable** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Performance metrics for NATS Subject Manager operations.  This module provides m** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Performance metrics for NATS Subject Manager operations.      Tracks validation** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record a validation operation.          Args:             duration: Time taken i** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record a build operation.          Args:             duration: Time taken in sec** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record an error occurrence.          Args:             error_type: Type of error** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Reset all metrics to zero.** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Predefined subject patterns for MythosMUD chat system.  This module contains all** (1 connections) — `server/services/nats_subject_manager/patterns.py`
- **Create SubjectManagerMetrics instance.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **Test SubjectManagerMetrics initialization.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`

## Relationships

- [manager subject services](manager_subject_services.md) (10 shared connections)
- [manager services nats](manager_services_nats.md) (6 shared connections)
- [subject nats manager](subject_nats_manager.md) (4 shared connections)
- [pattern matcher services](pattern_matcher_services.md) (1 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/tests/unit/services/nats_subject_manager/test_metrics.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*