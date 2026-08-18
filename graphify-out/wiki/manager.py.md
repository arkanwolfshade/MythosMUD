# manager.py

> 33 nodes

## Key Concepts

- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
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
- **NATS Subject Manager for MythosMUD. This module provides centralized subject…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Predefined subject patterns for MythosMUD chat system. This module contains all…** (1 connections) — `server/services/nats_subject_manager/patterns.py`
- **Subscription pattern utilities for NATS Subject Manager. This module provides…** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Convert a pattern template into a subscription pattern with wildcards. Args:…** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Get all chat-related subscription patterns. Args: patterns: Dictionary of…** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Get all event-related subscription patterns. Args: patterns: Dictionary of…** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Unit tests for NATS Subscription Patterns. Tests the subscription pattern…** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **Test get_event_subscription_patterns() handles missing patterns.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- *... and 8 more nodes in this community*

## Relationships

- [test_validation.py](test_validation.py.md) (12 shared connections)
- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (4 shared connections)
- [test_metrics.py](test_metrics.py.md) (2 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (2 shared connections)
- [subject_controller.py](subject_controller.py.md) (1 shared connections)
- [test_manager.py](test_manager.py.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 71 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*