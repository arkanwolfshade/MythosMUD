# test_look_item.py

> 45 nodes · cohesion 0.09

## Key Concepts

- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **test_subject_controller.py** (24 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **register_pattern()** (11 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (11 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (9 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (9 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (8 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **_admin_user()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_register_pattern_invalid()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **asyncio** (6 connections)
- **RegisterPatternResponse** (5 connections) — `server/api/admin/subject_controller.py`
- **test_register_pattern_success()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_invalid()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_valid()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **BaseModel** (4 connections)
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **test_get_patterns()** (4 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_request_schemas_reject_unknown_field()** (4 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **test_get_subject_statistics()** (3 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- *... and 20 more nodes in this community*

## Relationships

- [CircuitBreaker](CircuitBreaker.md) (12 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (9 shared connections)
- [AttributeError](AttributeError.md) (8 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (5 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (1 shared connections)
- [schema.sql](schema.sql.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/tests/unit/api/admin/test_subject_controller.py`

## Audit Trail

- EXTRACTED: 126 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*