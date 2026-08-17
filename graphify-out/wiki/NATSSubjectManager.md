# NATSSubjectManager

> 111 nodes

## Key Concepts

- **NATSSubjectManager** (58 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **test_subject_controller.py** (22 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **server/services/nats_subject_manager/__init__.py** (21 connections) — `server/services/nats_subject_manager/__init__.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (17 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **register_pattern()** (11 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (11 connections) — `server/api/admin/subject_controller.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_patterns()** (9 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (9 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (8 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **_admin_user()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_register_pattern_invalid()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **Any** (7 connections)
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **BaseModel** (6 connections)
- **asyncio** (6 connections)
- *... and 86 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (22 shared connections)
- [SubjectValidator](SubjectValidator.md) (21 shared connections)
- [test_manager.py](test_manager.py.md) (10 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (3 shared connections)
- [NATSError](NATSError.md) (3 shared connections)
- [SubjectManagerMetrics](SubjectManagerMetrics.md) (3 shared connections)
- [subject_manager](subject_manager.md) (3 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/infrastructure/nats_broker.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/api/admin/test_subject_controller.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 278 (93%)
- INFERRED: 22 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*