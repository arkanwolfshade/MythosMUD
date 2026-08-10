# Cursor Setup Guide

> 41 nodes

## Key Concepts

- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Any** (3 connections)
- **test_get_subscription_pattern_single_param()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_multiple_params()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_no_params()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns_missing_pattern()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns_missing_pattern()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_subject_validator_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_basic()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_components()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subscription_pattern()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **Subscription pattern utilities for NATS Subject Manager.  This module provides u** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Convert a pattern template into a subscription pattern with wildcards.      Args** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Get all chat-related subscription patterns.      Args:         patterns: Diction** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Get all event-related subscription patterns.      Args:         patterns: Dictio** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- *... and 16 more nodes in this community*

## Relationships

- [Cursor Rules Docker](Cursor_Rules_Docker.md) (13 shared connections)
- [NPC Combat Events](NPC_Combat_Events.md) (7 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 138 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*