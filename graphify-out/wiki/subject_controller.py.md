# subject_controller.py

> 43 nodes

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
- **test_get_subject_statistics()** (3 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_require_admin_user_allows_admin()** (3 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- *... and 18 more nodes in this community*

## Relationships

- [NATSSubjectManager](NATSSubjectManager.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (8 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [manager.py](manager.py.md) (1 shared connections)
- [test_manager.py](test_manager.py.md) (1 shared connections)
- [test_validation.py](test_validation.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/tests/unit/api/admin/test_subject_controller.py`

## Audit Trail

- EXTRACTED: 130 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*