# NATS Pattern Matcher

> 47 nodes · cohesion 0.05

## Key Concepts

- **test_pattern_matcher.py** (19 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **PatternMatcher** (14 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **.matches_any_pattern()** (4 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **pattern_matcher.py** (3 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **._components_match_pattern()** (3 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **pattern_matcher()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **strict_pattern_matcher()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_pattern_matcher_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_pattern_matcher_init_strict()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **test_components_match_pattern_exact()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_components_match_pattern_invalid_placeholder_value()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_components_match_pattern_mismatch()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_components_match_pattern_multiple_placeholders()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_components_match_pattern_numbers()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_components_match_pattern_placeholder()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_components_match_pattern_strict_allows_hyphens()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_components_match_pattern_strict_no_underscores()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_matches_any_pattern_different_length()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_matches_any_pattern_exact_match()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_matches_any_pattern_multiple_patterns()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_matches_any_pattern_no_match()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **test_matches_any_pattern_strict_validation()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`
- **Pattern matching utilities for NATS Subject Manager.  This module provides patte** (1 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **Matcher for validating subjects against registered patterns.** (1 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- *... and 22 more nodes in this community*

## Relationships

- [[NATS Subject Exceptions]] (2 shared connections)
- [[Manager Services Nats]] (2 shared connections)
- [[NATS Subject Manager]] (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/pattern_matcher.py`
- `server/tests/unit/services/nats_subject_manager/test_pattern_matcher.py`

## Audit Trail

- EXTRACTED: 105 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
