# Test Subscription Patterns

> 58 nodes

## Key Concepts

- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **SubjectValidationError** (22 connections) — `server/services/nats_subject_manager/exceptions.py`
- **server/services/nats_subject_manager/__init__.py** (20 connections) — `server/services/nats_subject_manager/__init__.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_parameter_value()** (5 connections) — `server/services/nats_subject_manager/validation.py`
- **nats_subject_manager/metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **.validate_pattern_params()** (4 connections) — `server/services/nats_subject_manager/validation.py`
- **test_get_chat_subscription_patterns()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns_missing_pattern()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns_missing_pattern()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_multiple_params()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_no_params()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_single_param()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **patterns.py** (3 connections) — `server/services/nats_subject_manager/patterns.py`
- **Any** (3 connections)
- *... and 33 more nodes in this community*

## Relationships

- [Test Nats Subject Exceptions](Test_Nats_Subject_Exceptions.md) (17 shared connections)
- [Test Validation](Test_Validation.md) (10 shared connections)
- [Test Manager](Test_Manager.md) (7 shared connections)
- [Test Metrics](Test_Metrics.md) (4 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (3 shared connections)
- [Test Pattern Matcher](Test_Pattern_Matcher.md) (3 shared connections)
- [NATS Service Client](NATS_Service_Client.md) (2 shared connections)
- [Chat Service & Channels](Chat_Service_&_Channels.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Manager](Manager.md) (1 shared connections)
- [Subject Controller](Subject_Controller.md) (1 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 141 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*