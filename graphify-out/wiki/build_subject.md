# .build_subject

> 17 nodes · cohesion 0.15

## Key Concepts

- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
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

- [CombatService](CombatService.md) (8 shared connections)
- [PatternNotFoundError](PatternNotFoundError.md) (4 shared connections)
- [SubjectValidationError](SubjectValidationError.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/manager.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*