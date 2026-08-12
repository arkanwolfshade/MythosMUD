# test_metrics.py

> 66 nodes

## Key Concepts

- **test_metrics.py** (27 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **._calculate_percentile()** (6 connections) — `server/services/nats_subject_manager/metrics.py`
- **.get_metrics()** (4 connections) — `server/services/nats_subject_manager/metrics.py`
- **metrics()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_multiple_values()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_single_value()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_subject_manager_metrics_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **.record_build()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_error()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_validation()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.reset()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_build_times_maxlen()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_get_metrics_calculates_percentiles()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_get_metrics_empty()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_get_metrics_with_data()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_build_failure()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_build_multiple()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_build_stores_times()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_build_success()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_error_missing_parameter()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_error_pattern_not_found()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_error_unknown()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_error_validation_error()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- *... and 41 more nodes in this community*

## Relationships

- [SubjectValidator](SubjectValidator.md) (4 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/services/nats_subject_manager/test_metrics.py`

## Audit Trail

- EXTRACTED: 148 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*