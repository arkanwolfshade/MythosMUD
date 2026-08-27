# docker Best Practices

> 14 nodes

## Key Concepts

- **test_profession.py** (30 connections) — `server/tests/unit/models/test_profession.py`
- **Test meets_stat_requirements returns True when all requirements are met.** (5 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_requirement_display_text_single_requirement()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_empty_string()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_meets_stat_requirements_all_met()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_meets_stat_requirements_empty_requirements()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_meets_stat_requirements_exact_match()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_meets_stat_requirements_extra_stats()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_meets_stat_requirements_invalid_json()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_meets_stat_requirements_multiple_not_met()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **Unit tests for the Profession model. Tests the Profession model methods…** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test meets_stat_requirements returns False when multiple requirements are not…** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_requirement_display_text formats single requirement correctly.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_stat_requirements returns empty dict for empty string.** (1 connections) — `server/tests/unit/models/test_profession.py`

## Relationships

- [required](required.md) (13 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [markdownlint-cli](markdownlint-cli.md) (1 shared connections)
- [test_connection_manager_lazy_load_called](test_connection_manager_lazy_load_called.md) (1 shared connections)
- [test_broadcast_player_death_personal_message_error](test_broadcast_player_death_personal_message_error.md) (1 shared connections)
- [test_broadcast_player_mortally_wounded_personal_message_error](test_broadcast_player_mortally_wounded_personal_message_error.md) (1 shared connections)
- [patch-package](patch-package.md) (1 shared connections)
- [test_send_dp_decay_message_error](test_send_dp_decay_message_error.md) (1 shared connections)
- [test_connection_manager_setter](test_connection_manager_setter.md) (1 shared connections)
- [@playwright/test](@playwright-test.md) (1 shared connections)
- [tailwindcss](tailwindcss.md) (1 shared connections)
- [unit/realtime/maintenance/__init__.py](unit-realtime-maintenance-__init__.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/models/test_profession.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*