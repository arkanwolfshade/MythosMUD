# Manager Services Nats

> 67 nodes

## Key Concepts

- **test_metrics.py** (27 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **._calculate_percentile()** (6 connections) — `server/services/nats_subject_manager/metrics.py`
- **metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **.get_metrics()** (4 connections) — `server/services/nats_subject_manager/metrics.py`
- **metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_subject_manager_metrics_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_single_value()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_multiple_values()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **.record_validation()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_build()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.record_error()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **.reset()** (2 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_record_validation_success()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_validation_failure()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_validation_cache_hit()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_validation_multiple()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_validation_stores_times()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_build_success()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_build_failure()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_build_multiple()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_build_stores_times()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_error_pattern_not_found()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_record_error_missing_parameter()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- *... and 42 more nodes in this community*

## Relationships

- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (3 shared connections)
- [Cursor Setup Guide](Cursor_Setup_Guide.md) (2 shared connections)
- [NATS Pattern Matcher](NATS_Pattern_Matcher.md) (1 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/services/nats_subject_manager/test_metrics.py`

## Audit Trail

- EXTRACTED: 152 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*