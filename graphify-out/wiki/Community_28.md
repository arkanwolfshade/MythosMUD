# Community 28

> 167 nodes

## Key Concepts

- **NATSSubjectManager** (59 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **test_subject_controller.py** (24 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **SubjectValidationError** (22 connections) — `server/services/nats_subject_manager/exceptions.py`
- **server/services/nats_subject_manager/__init__.py** (20 connections) — `server/services/nats_subject_manager/__init__.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **event_publisher.py** (14 connections) — `server/realtime/event_publisher.py`
- **PatternMatcher** (13 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **register_pattern()** (11 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (11 connections) — `server/api/admin/subject_controller.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_patterns()** (9 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (9 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (8 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- *... and 142 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (14 shared connections)
- [Community 1249](Community_1249.md) (11 shared connections)
- [Community 649](Community_649.md) (11 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (9 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (8 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (7 shared connections)
- [NATS Configuration](NATS_Configuration.md) (7 shared connections)
- [Community 483](Community_483.md) (6 shared connections)
- [Community 1137](Community_1137.md) (5 shared connections)
- [Community 1250](Community_1250.md) (4 shared connections)
- [Combat Events](Combat_Events.md) (3 shared connections)
- [Community 1364](Community_1364.md) (3 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/realtime/event_publisher.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/pattern_matcher.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/api/admin/test_subject_controller.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 398 (94%)
- INFERRED: 25 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*