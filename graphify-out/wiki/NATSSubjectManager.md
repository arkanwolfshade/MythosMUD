# NATSSubjectManager

> 63 nodes

## Key Concepts

- **NATSSubjectManager** (59 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **test_subject_controller.py** (22 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
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
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **test_get_patterns()** (4 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- *... and 38 more nodes in this community*

## Relationships

- [SubjectValidator](SubjectValidator.md) (14 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (13 shared connections)
- [test_manager.py](test_manager.py.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [.build_subject](build_subject.md) (8 shared connections)
- [NATSService](NATSService.md) (5 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [NATSPublishError](NATSPublishError.md) (3 shared connections)
- [event_publisher.py](event_publisher.py.md) (2 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/api/admin/test_subject_controller.py`

## Audit Trail

- EXTRACTED: 177 (92%)
- INFERRED: 16 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*