# subject_controller.py

> 25 nodes · cohesion 0.12

## Key Concepts

- **subject_controller.py** (26 connections) — `server/api/admin/subject_controller.py`
- **register_pattern()** (9 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (7 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (6 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (6 connections) — `server/api/admin/subject_controller.py`
- **BaseModel** (6 connections)
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **NATS Subject Management API Controller for MythosMUD.  This module provides REST** (1 connections) — `server/api/admin/subject_controller.py`
- **Get NATS subject management statistics and health status.      This endpoint pro** (1 connections) — `server/api/admin/subject_controller.py`
- **Validate a NATS subject against registered patterns.      This endpoint allows a** (1 connections) — `server/api/admin/subject_controller.py`
- **Get all registered subject patterns.      This endpoint allows administrators to** (1 connections) — `server/api/admin/subject_controller.py`
- **Register a new subject pattern.      This endpoint allows administrators to dyna** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject management statistics.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern listing.** (1 connections) — `server/api/admin/subject_controller.py`
- **Dependency function to inject NATSSubjectManager.      Returns:         Global N** (1 connections) — `server/api/admin/subject_controller.py`

## Relationships

- [ErrorContext](ErrorContext.md) (6 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [PatternNotFoundError](PatternNotFoundError.md) (4 shared connections)
- [User](User.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (1 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`

## Audit Trail

- EXTRACTED: 97 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*