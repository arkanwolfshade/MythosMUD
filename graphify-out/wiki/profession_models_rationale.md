# profession models rationale

> 20 nodes

## Key Concepts

- **test_profession.py** (30 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_empty_string()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_set_stat_requirements()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_mechanical_effects_invalid_json()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_mechanical_effects_empty_string()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_meets_stat_requirements_missing_stat()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_is_available_for_selection_true()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_is_available_for_selection_false()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_requirement_display_text_single_requirement()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_requirement_display_text_multiple_requirements()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **Unit tests for the Profession model.  Tests the Profession model methods includi** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_stat_requirements returns empty dict for empty string.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test set_stat_requirements stores dict as JSON string.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_mechanical_effects returns empty dict for invalid JSON.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_mechanical_effects returns empty dict for empty string.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test meets_stat_requirements returns False when required stat is missing.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test is_available_for_selection returns True when is_available is True.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test is_available_for_selection returns False when is_available is False.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_requirement_display_text formats single requirement correctly.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_requirement_display_text formats multiple requirements correctly.** (1 connections) — `server/tests/unit/models/test_profession.py`

## Relationships

- [persistence core infrastructure](persistence_core_infrastructure.md) (13 shared connections)
- [room toolkit validator](room_toolkit_validator.md) (2 shared connections)
- [realtime player event](realtime_player_event.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (1 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (1 shared connections)
- [archive LOGGING BEST](archive_LOGGING_BEST.md) (1 shared connections)
- [static schemas room](static_schemas_room.md) (1 shared connections)
- [archive AUDIT EXECUTIVE](archive_AUDIT_EXECUTIVE.md) (1 shared connections)
- [archive 2025 REMEDIATION](archive_2025_REMEDIATION.md) (1 shared connections)
- [player realtime event](player_realtime_event.md) (1 shared connections)
- [commands remediation cursor](commands_remediation_cursor.md) (1 shared connections)

## Source Files

- `server/tests/unit/models/test_profession.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*