# Warning Fixes Session

> 23 nodes

## Key Concepts

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
- **Request model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject management statistics.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern listing.** (1 connections) — `server/api/admin/subject_controller.py`
- **Get NATS subject management statistics and health status.      This endpoint p** (1 connections) — `server/api/admin/subject_controller.py`
- **Validate a NATS subject against registered patterns.** (1 connections) — `server/api/admin/subject_controller.py`
- **Get all registered subject patterns.      This endpoint allows administrators** (1 connections) — `server/api/admin/subject_controller.py`
- **Register a new subject pattern.** (1 connections) — `server/api/admin/subject_controller.py`
- **Register a new subject pattern.** (1 connections) — `server/api/admin/subject_controller.py`

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (11 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (5 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (4 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (4 shared connections)
- [Cursor Rules Docker](Cursor_Rules_Docker.md) (2 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`

## Audit Trail

- EXTRACTED: 76 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*