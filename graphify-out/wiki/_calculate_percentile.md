# ._calculate_percentile

> 11 nodes

## Key Concepts

- **._calculate_percentile()** (6 connections) — `server/services/nats_subject_manager/metrics.py`
- **.get_metrics()** (4 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_calculate_percentile_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_multiple_values()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **test_calculate_percentile_single_value()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **Any** (1 connections)
- **Get current metrics summary. Returns: Dictionary containing all metrics** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Calculate percentile from list of times. Args: times: List of time measurements…** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Test _calculate_percentile() returns 0 for empty list.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **Test _calculate_percentile() handles single value.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`
- **Test _calculate_percentile() calculates percentile correctly.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_metrics.py`

## Relationships

- [test_metrics.py](test_metrics.py.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)

## Source Files

- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/services/nats_subject_manager/test_metrics.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*