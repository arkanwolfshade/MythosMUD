# manager subject services

> 38 nodes

## Key Concepts

- **subject_controller.py** (27 connections) — `server/api/admin/subject_controller.py`
- **test_subject_controller.py** (21 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **register_pattern()** (12 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (10 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (8 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (8 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **_admin_user()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **BaseModel** (6 connections)
- **test_register_pattern_invalid()** (6 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **test_validate_subject_valid()** (4 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_invalid()** (4 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_register_pattern_success()** (4 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **test_require_admin_user_rejects_non_admin()** (3 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_require_admin_user_allows_admin()** (3 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_get_patterns()** (3 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_get_subject_statistics()** (2 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **NATS Subject Management API Controller for MythosMUD.  This module provides REST** (1 connections) — `server/api/admin/subject_controller.py`
- *... and 13 more nodes in this community*

## Relationships

- [commands communication support](commands_communication_support.md) (12 shared connections)
- [Exception Containers](Exception_Containers.md) (9 shared connections)
- [Spell Validation](Spell_Validation.md) (6 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/tests/unit/api/admin/test_subject_controller.py`

## Audit Trail

- EXTRACTED: 178 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*