# test nats message handler

> 51 nodes

## Key Concepts

- **PatternNotFoundError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **InvalidPatternError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **register_pattern()** (9 connections) — `server/api/admin/subject_controller.py`
- **test_exception_hierarchy()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_caught_by_base()** (5 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_pattern_not_found_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_invalid_pattern_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_subject_validation_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_pattern_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_missing_parameter()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_register_pattern_duplicate_name()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_register_pattern_invalid_format()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_register_pattern_missing_placeholder()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_pattern_info_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_subscription_pattern_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_multiple()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/exceptions.py`
- *... and 26 more nodes in this community*

## Relationships

- [Any](Any.md) (17 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (10 shared connections)
- [test corpse lifecycle service](test_corpse_lifecycle_service.md) (10 shared connections)
- [metrics](metrics.md) (3 shared connections)
- [test clear corrupted cache entry](test_clear_corrupted_cache_entry.md) (2 shared connections)
- [fetch schedule entries()](fetch_schedule_entries%28%29.md) (1 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 159 (83%)
- INFERRED: 33 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*