# Cursor Setup Guide

> 45 nodes

## Key Concepts

- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **patterns.py** (3 connections) — `server/services/nats_subject_manager/patterns.py`
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
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_basic()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_components()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subscription_pattern()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **NATS Subject Manager for MythosMUD.  This module provides centralized subject na** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Predefined subject patterns for MythosMUD chat system.  This module contains all** (1 connections) — `server/services/nats_subject_manager/patterns.py`
- *... and 20 more nodes in this community*

## Relationships

- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (15 shared connections)
- [NPC Combat Events](NPC_Combat_Events.md) (8 shared connections)
- [NATS Pattern Matcher](NATS_Pattern_Matcher.md) (3 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (2 shared connections)
- [Cursor Skills Critique](Cursor_Skills_Critique.md) (2 shared connections)
- [Inventory Test Support](Inventory_Test_Support.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 167 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*