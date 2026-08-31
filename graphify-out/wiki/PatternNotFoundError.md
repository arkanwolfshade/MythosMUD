# PatternNotFoundError

> 33 nodes

## Key Concepts

- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (17 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **test_invalid_pattern_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_multiple()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_nats_subject_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_pattern_not_found_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_subject_validation_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/exceptions.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Exception** (1 connections)
- **Base exception for NATS subject-related errors.** (1 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Exception raised when a pattern name is not found in registry.** (1 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Exception raised when required parameters are missing.** (1 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Exception raised when a pattern format is invalid.** (1 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Register a new subject pattern. Args: name: Unique name for the pattern…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Unit tests for NATS Subject Manager Exceptions. Tests the exception classes.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **Test exceptions can be caught by base class.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- *... and 8 more nodes in this community*

## Relationships

- [SubjectValidator](SubjectValidator.md) (13 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (9 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_manager.py](test_manager.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 80 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*