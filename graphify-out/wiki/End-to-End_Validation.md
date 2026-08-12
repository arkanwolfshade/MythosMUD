# End-to-End Validation

> 29 nodes

## Key Concepts

- **subject_controller.py** (27 connections) — `server/api/admin/subject_controller.py`
- **register_pattern()** (10 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (7 connections) — `server/api/admin/subject_controller.py`
- **BaseModel** (6 connections)
- **get_subject_statistics()** (6 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (6 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (6 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (5 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternResponse** (5 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (4 connections) — `server/api/admin/subject_controller.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **NATS Subject Management API Controller for MythosMUD.  This module provides RE** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject management statistics.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern listing.** (1 connections) — `server/api/admin/subject_controller.py`
- **Dependency function to inject NATSSubjectManager.      Returns:         Globa** (1 connections) — `server/api/admin/subject_controller.py`
- **Dependency to require admin permissions.      Args:         current_user: Cur** (1 connections) — `server/api/admin/subject_controller.py`
- **Get NATS subject management statistics and health status.      This endpoint p** (1 connections) — `server/api/admin/subject_controller.py`
- *... and 4 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (7 shared connections)
- [Services Rescue Service](Services_Rescue_Service.md) (7 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (6 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`

## Audit Trail

- EXTRACTED: 113 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*