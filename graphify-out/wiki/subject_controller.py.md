# subject_controller.py

> 47 nodes

## Key Concepts

- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **test_subject_controller.py** (22 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **register_pattern()** (11 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (11 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (9 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (9 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (8 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **_admin_user()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_register_pattern_invalid()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **BaseModel** (6 connections)
- **asyncio** (6 connections)
- **RegisterPatternResponse** (5 connections) — `server/api/admin/subject_controller.py`
- **test_register_pattern_success()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_invalid()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_valid()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **test_get_patterns()** (4 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 22 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (14 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (11 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (8 shared connections)
- [PatternNotFoundError](PatternNotFoundError.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [SubjectValidator](SubjectValidator.md) (2 shared connections)
- [test_manager.py](test_manager.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/api/admin/test_subject_controller.py`

## Audit Trail

- EXTRACTED: 134 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*