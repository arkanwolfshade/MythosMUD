# commands lucidity recovery

> 23 nodes

## Key Concepts

- **subject_controller.py** (26 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (7 connections) — `server/api/admin/subject_controller.py`
- **BaseModel** (6 connections)
- **get_subject_statistics()** (6 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (6 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (4 connections) — `server/api/admin/subject_controller.py`
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
- **Get all registered subject patterns.      This endpoint allows administrators to** (1 connections) — `server/api/admin/subject_controller.py`

## Relationships

- [manager subject services](manager_subject_services.md) (5 shared connections)
- [subject validation services](subject_validation_services.md) (5 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (5 shared connections)
- [Exception Containers](Exception_Containers.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [admin auth service](admin_auth_service.md) (1 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [logging file setup](logging_file_setup.md) (1 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`

## Audit Trail

- EXTRACTED: 90 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*