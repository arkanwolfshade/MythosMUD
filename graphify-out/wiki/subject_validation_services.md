# subject validation services

> 37 nodes

## Key Concepts

- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **__init__.py** (12 connections) — `server/services/nats_subject_manager/__init__.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
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
- **NATS Subject Manager for MythosMUD.  This package provides centralized subject n** (1 connections) — `server/services/nats_subject_manager/__init__.py`
- **NATS Subject Manager for MythosMUD.  This module provides centralized subject na** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Performance metrics for NATS Subject Manager operations.  This module provides m** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Predefined subject patterns for MythosMUD chat system.  This module contains all** (1 connections) — `server/services/nats_subject_manager/patterns.py`
- **Subscription pattern utilities for NATS Subject Manager.  This module provides u** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Convert a pattern template into a subscription pattern with wildcards.      Args** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- *... and 12 more nodes in this community*

## Relationships

- [zone npc config](zone_npc_config.md) (14 shared connections)
- [manager subject services](manager_subject_services.md) (5 shared connections)
- [commands communication support](commands_communication_support.md) (5 shared connections)
- [manager services nats](manager_services_nats.md) (4 shared connections)
- [pattern matcher services](pattern_matcher_services.md) (2 shared connections)

## Source Files

- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 144 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*