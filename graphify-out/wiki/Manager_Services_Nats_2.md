# Manager Services Nats

> 17 nodes · cohesion 0.15

## Key Concepts

- **Any** (14 connections) — `server/services/nats_subject_manager/manager.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_performance_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **Build a NATS subject from a pattern and parameters.          Args:             p** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Ensure pattern exists in registry.          Args:             pattern_name: Name** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Ensure all required parameters are provided.          Args:             pattern_** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Format subject string from pattern and parameters.          Args:             pa** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Ensure subject length is within limits.          Args:             subject: Subj** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Get information about a registered pattern.          Args:             pattern_n** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Get all registered patterns.          Returns:             Dictionary of all reg** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Get current performance metrics.          Returns:             Dictionary contai** (1 connections) — `server/services/nats_subject_manager/manager.py`

## Relationships

- [[NATS Subject Exceptions]] (9 shared connections)
- [[NATS Subject Manager]] (8 shared connections)
- [[Manager Services Nats]] (1 shared connections)
- [[NATS Pattern Matcher]] (1 shared connections)
- [[NATS Subject Validator Tests]] (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/manager.py`

## Audit Trail

- EXTRACTED: 53 (88%)
- INFERRED: 7 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
