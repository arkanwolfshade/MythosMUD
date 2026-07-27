# NATS Subject Admin API

> 29 nodes · cohesion 0.09

## Key Concepts

- **subject_controller.py** (25 connections) — `server/api/admin/subject_controller.py`
- **register_pattern()** (7 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (7 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (6 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (6 connections) — `server/api/admin/subject_controller.py`
- **NATSSubjectManager** (5 connections) — `server/api/admin/subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **__init__.py** (3 connections) — `server/api/admin/__init__.py`
- **NATS Subject Management API Controller for MythosMUD.  This module provides REST** (1 connections) — `server/api/admin/subject_controller.py`
- **Dependency to require admin permissions.      Args:         current_user: Curren** (1 connections) — `server/api/admin/subject_controller.py`
- **Get NATS subject management statistics and health status.      This endpoint pro** (1 connections) — `server/api/admin/subject_controller.py`
- **Validate a NATS subject against registered patterns.      This endpoint allows a** (1 connections) — `server/api/admin/subject_controller.py`
- **Get all registered subject patterns.      This endpoint allows administrators to** (1 connections) — `server/api/admin/subject_controller.py`
- **Register a new subject pattern.      This endpoint allows administrators to dyna** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- *... and 4 more nodes in this community*

## Relationships

- [[NPC Admin API]] (6 shared connections)
- [[Standardized Error Responses]] (6 shared connections)
- [[Container Exception Handlers]] (6 shared connections)
- [[Admin NPC Schemas]] (6 shared connections)
- [[NATS Subject Exceptions]] (2 shared connections)
- [[API Test Fixtures]] (1 shared connections)
- [[NATS Subject Manager]] (1 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/subject_controller.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
