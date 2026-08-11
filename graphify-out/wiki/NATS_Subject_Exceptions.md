# NATS Subject Exceptions

> 70 nodes

## Key Concepts

- **NATSSubjectManager** (57 connections) — `server/services/nats_subject_manager/manager.py`
- **SubjectValidationError** (29 connections) — `server/services/nats_subject_manager/exceptions.py`
- **PatternNotFoundError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **InvalidPatternError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **__init__.py** (12 connections) — `server/services/nats_subject_manager/__init__.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **test_exception_hierarchy()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **test_exceptions_can_be_caught_by_base()** (5 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_subject_too_long()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_pattern_not_found_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_invalid_pattern_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_subject_validation_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- *... and 45 more nodes in this community*

## Relationships

- [Inventory Test Support](Inventory_Test_Support.md) (23 shared connections)
- [Cursor Setup Guide](Cursor_Setup_Guide.md) (15 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (12 shared connections)
- [NPC Combat Events](NPC_Combat_Events.md) (7 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (3 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (3 shared connections)
- [Services Rescue Service](Services_Rescue_Service.md) (3 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (2 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (2 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (2 shared connections)
- [NATS Pattern Matcher](NATS_Pattern_Matcher.md) (2 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 298 (88%)
- INFERRED: 42 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*