# Manager Services Nats

> 21 nodes · cohesion 0.10

## Key Concepts

- **SubjectManagerMetrics** (17 connections) — `server/services/nats_subject_manager/metrics.py`
- **.__init__()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_metrics()** (4 connections) — `server/services/nats_subject_manager/metrics.py`
- **._calculate_percentile()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_subject_manager_metrics_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **.record_build()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_error()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_validation()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.reset()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **Initialize NATS Subject Manager.          Args:             enable_cache: Enable** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Get current metrics summary.          Returns:             Dictionary containing** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Calculate percentile from list of times.          Args:             times: List** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Reset all metrics to zero.** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Performance metrics for NATS Subject Manager operations.      Tracks validation** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record a validation operation.          Args:             duration: Time taken i** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record a build operation.          Args:             duration: Time taken in sec** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record an error occurrence.          Args:             error_type: Type of error** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Create SubjectManagerMetrics instance.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **Test SubjectManagerMetrics initialization.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **Any** (1 connections) — `server/services/nats_subject_manager/metrics.py`

## Relationships

- [[NATS Subject Exceptions]] (3 shared connections)
- [[NATS Subject Metrics]] (3 shared connections)
- [[NATS Subject Manager]] (2 shared connections)
- [[NATS Pattern Matcher]] (1 shared connections)
- [[NATS Subject Validator Tests]] (1 shared connections)
- [[Manager Services Nats]] (1 shared connections)
- [[Message Queue Cleanup]] (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/services/nats_subject_manager/test_metrics.py`

## Audit Trail

- EXTRACTED: 52 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
