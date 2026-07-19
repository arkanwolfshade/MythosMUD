# NATS Subject Manager

> 93 nodes · cohesion 0.02

## Key Concepts

- **NATSSubjectManager** (46 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (46 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **Test NATSSubjectManager initialization without metrics.** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_subject_too_long()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_strict_validation()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.clear_cache()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_chat_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_event_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **Get all chat-related subscription patterns.          Returns:             List o** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **Get all event-related subscription patterns.          Returns:             List** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **Test get_event_subscription_patterns() returns event patterns.** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_invalid_parameter_value()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_missing_parameter()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- *... and 68 more nodes in this community*

## Relationships

- [[NATS Subject Exceptions]] (15 shared connections)
- [[Manager Services Nats]] (10 shared connections)
- [[Combat Domain Events]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Combat Service Bundle]] (2 shared connections)
- [[NATS Subject Validator]] (2 shared connections)
- [[NATS Subject Admin API]] (1 shared connections)
- [[Message Broker Errors]] (1 shared connections)
- [[NATS Pattern Matcher]] (1 shared connections)
- [[NATS Subject Validator Tests]] (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 243 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
