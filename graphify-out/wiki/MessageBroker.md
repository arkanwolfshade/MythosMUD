# MessageBroker

> 21 nodes

## Key Concepts

- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **test_get_chat_subscription_patterns()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns_missing_pattern()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns_missing_pattern()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_multiple_params()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_no_params()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_single_param()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_event_subscription_patterns() returns event patterns.** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Get all event-related subscription patterns. Args: patterns: Dictionary of…** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Unit tests for NATS Subscription Patterns. Tests the subscription pattern…** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_event_subscription_patterns() handles missing patterns.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_chat_subscription_patterns() returns empty list when no chat patterns.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_subscription_pattern() replaces single parameter.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_subscription_pattern() replaces multiple parameters.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_subscription_pattern() returns pattern unchanged when no params.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_chat_subscription_patterns() returns chat patterns.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_chat_subscription_patterns() handles missing patterns.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Relationships

- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (14 shared connections)

## Source Files

- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*