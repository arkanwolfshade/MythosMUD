# SubjectManagerMetrics

> 30 nodes

## Key Concepts

- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **._calculate_percentile()** (6 connections) — `server/services/nats_subject_manager/metrics.py`
- **nats_subject_manager/metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **.get_metrics()** (4 connections) — `server/services/nats_subject_manager/metrics.py`
- **metrics()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_calculate_percentile_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_multiple_values()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_single_value()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_subject_manager_metrics_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **.record_build()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_error()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_validation()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.reset()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **Any** (1 connections)
- **fixture** (1 connections)
- **Performance metrics for NATS Subject Manager operations. This module provides…** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Get current metrics summary. Returns: Dictionary containing all metrics** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Calculate percentile from list of times. Args: times: List of time measurements…** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Reset all metrics to zero.** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Performance metrics for NATS Subject Manager operations. Tracks validation…** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Initialize metrics collection.** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record a validation operation. Args: duration: Time taken in seconds success:…** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record a build operation. Args: duration: Time taken in seconds success:…** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Record an error occurrence. Args: error_type: Type of error (pattern_not_found,…** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- *... and 5 more nodes in this community*

## Relationships

- [test_metrics.py](test_metrics.py.md) (7 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [SubjectValidator](SubjectValidator.md) (2 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/services/nats_subject_manager/test_metrics.py`

## Audit Trail

- EXTRACTED: 42 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*