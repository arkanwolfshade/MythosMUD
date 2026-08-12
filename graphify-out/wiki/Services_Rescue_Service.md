# Services Rescue Service

> 41 nodes

## Key Concepts

- **NATSSubjectManager** (57 connections) — `server/services/nats_subject_manager/manager.py`
- **MissingParameterError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **subject_manager()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_performance_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.get_chat_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_event_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.clear_cache()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **Initialize combat event publisher.          Args:             nats_service: N** (1 connections) — `server/services/combat_event_publisher.py`
- **Exception raised when required parameters are missing.** (1 connections) — `server/services/nats_subject_manager/exceptions.py`
- **Manager for NATS subject patterns and validation.      This class provides centr** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Build a NATS subject from a pattern and parameters.          Args:             p** (1 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 16 more nodes in this community*

## Relationships

- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (14 shared connections)
- [Inventory Test Support](Inventory_Test_Support.md) (12 shared connections)
- [Cursor Setup Guide](Cursor_Setup_Guide.md) (8 shared connections)
- [End-to-End Validation](End-to-End_Validation.md) (7 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (2 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (2 shared connections)
- [NATS Pattern Matcher](NATS_Pattern_Matcher.md) (2 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 158 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*