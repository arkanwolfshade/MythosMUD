# Async Persistence Migration

> 20 nodes · cohesion 0.10

## Key Concepts

- **test_profession.py** (30 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_mechanical_effects_empty_string()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_mechanical_effects_invalid_json()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_requirement_display_text_multiple_requirements()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_requirement_display_text_single_requirement()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_empty_string()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_is_available_for_selection_false()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_is_available_for_selection_true()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_meets_stat_requirements_missing_stat()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_set_stat_requirements()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **Unit tests for the Profession model.  Tests the Profession model methods includi** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_mechanical_effects returns empty dict for invalid JSON.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_mechanical_effects returns empty dict for empty string.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test meets_stat_requirements returns False when required stat is missing.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test is_available_for_selection returns True when is_available is True.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test is_available_for_selection returns False when is_available is False.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_requirement_display_text formats single requirement correctly.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_requirement_display_text formats multiple requirements correctly.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_stat_requirements returns empty dict for empty string.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test set_stat_requirements stores dict as JSON string.** (1 connections) — `server/tests/unit/models/test_profession.py`

## Relationships

- [WebSocket Code Review](WebSocket_Code_Review.md) (13 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Cursor Plans Gladiator](Cursor_Plans_Gladiator.md) (1 shared connections)
- [Services Feature Flag](Services_Feature_Flag.md) (1 shared connections)
- [Investigations Sessions Message](Investigations_Sessions_Message.md) (1 shared connections)
- [Cursor Plans Authority](Cursor_Plans_Authority.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Cursor Skills Quieter](Cursor_Skills_Quieter.md) (1 shared connections)
- [Liability . Call ()](Liability_._Call_%28%29.md) (1 shared connections)
- [Room Toolkit Validator](Room_Toolkit_Validator.md) (1 shared connections)

## Source Files

- `server/tests/unit/models/test_profession.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*