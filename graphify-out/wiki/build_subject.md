# .build_subject

> 17 nodes

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
- **Build a NATS subject from a pattern and parameters. Args: pattern_name: Name of…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Ensure pattern exists in registry. Args: pattern_name: Name of the pattern to…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Ensure all required parameters are provided. Args: pattern_name: Name of the…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Format subject string from pattern and parameters. Args: pattern_name: Name of…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Ensure subject length is within limits. Args: subject: Subject string to…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Get information about a registered pattern. Args: pattern_name: Name of the…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Get all registered patterns. Returns: Dictionary of all registered patterns…** (1 connections) — `server/services/nats_subject_manager/manager.py`
- **Get current performance metrics. Returns: Dictionary containing performance…** (1 connections) — `server/services/nats_subject_manager/manager.py`

## Relationships

- [NATSSubjectManager](NATSSubjectManager.md) (8 shared connections)
- [SubjectValidator](SubjectValidator.md) (5 shared connections)

## Source Files

- `server/services/nats_subject_manager/manager.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*