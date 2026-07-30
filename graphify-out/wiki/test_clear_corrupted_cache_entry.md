# test clear corrupted cache entry

> 19 nodes

## Key Concepts

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
- **Request model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject validation.** (1 connections) — `server/api/admin/subject_controller.py`
- **Request model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern registration.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for subject management statistics.** (1 connections) — `server/api/admin/subject_controller.py`
- **Response model for pattern listing.** (1 connections) — `server/api/admin/subject_controller.py`
- **Get NATS subject management statistics and health status.      This endpoint pro** (1 connections) — `server/api/admin/subject_controller.py`
- **Validate a NATS subject against registered patterns.      This endpoint allows a** (1 connections) — `server/api/admin/subject_controller.py`
- **Get all registered subject patterns.      This endpoint allows administrators to** (1 connections) — `server/api/admin/subject_controller.py`

## Relationships

- [metrics](metrics.md) (9 shared connections)
- [fetch schedule entries()](fetch_schedule_entries%28%29.md) (3 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (3 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (3 shared connections)
- [test nats message handler](test_nats_message_handler.md) (2 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*