# commands communication support

> 39 nodes

## Key Concepts

- **PatternNotFoundError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exception_hierarchy()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_caught_by_base()** (5 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_pattern_not_found_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_invalid_pattern_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_subject_validation_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_pattern_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_missing_parameter()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_pattern_info_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_subscription_pattern_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_multiple()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/exceptions.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Exception** (1 connections)
- **Base exception for NATS subject-related errors.** (1 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Exception raised when a pattern name is not found in registry.** (1 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Exception raised when required parameters are missing.** (1 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Get a subscription pattern with wildcards for NATS subscriptions.          This** (1 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 14 more nodes in this community*

## Relationships

- [manager subject services](manager_subject_services.md) (20 shared connections)
- [zone npc config](zone_npc_config.md) (12 shared connections)
- [subject validation services](subject_validation_services.md) (2 shared connections)

## Source Files

- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 125 (84%)
- INFERRED: 23 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*