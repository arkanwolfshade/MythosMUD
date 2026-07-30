# test clear corrupted cache entry

> 27 nodes

## Key Concepts

- **subject_controller.py** (26 connections) — `server/api/admin/subject_controller.py`
- **register_pattern()** (9 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (7 connections) — `server/api/admin/subject_controller.py`
- **BaseModel** (6 connections)
- **get_subject_statistics()** (6 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (6 connections) — `server/api/admin/subject_controller.py`
- **__init__.py** (4 connections) — `server/api/admin/__init__.py`
- **ValidateSubjectRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (4 connections) — `server/api/admin/subject_controller.py`
- **Admin API module for MythosMUD.  This module provides administrative API endpoin** (1 connections) — `server/api/admin/__init__.py`
- **NATS Subject Management API Controller for MythosMUD.  This module provides REST** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject management statistics.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern listing.** (1 connections) — `server/api/admin/subject_controller.py`
- **Dependency to require admin permissions.      Args:         current_user: Curren** (1 connections) — `server/api/admin/subject_controller.py`
- **Get NATS subject management statistics and health status.      This endpoint pro** (1 connections) — `server/api/admin/subject_controller.py`
- **Validate a NATS subject against registered patterns.      This endpoint allows a** (1 connections) — `server/api/admin/subject_controller.py`
- *... and 2 more nodes in this community*

## Relationships

- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (6 shared connections)
- [Any](Any.md) (4 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [init](init.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/subject_controller.py`

## Audit Trail

- EXTRACTED: 103 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*