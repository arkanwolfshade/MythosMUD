# profession models rationale

> 120 nodes

## Key Concepts

- **Profession** (54 connections) — `server/models/profession.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_profession.py** (30 connections) — `server/tests/unit/models/test_profession.py`
- **Any** (8 connections)
- **.get_stat_requirements()** (5 connections) — `server/models/profession.py`
- **.set_stat_requirements()** (3 connections) — `server/models/profession.py`
- **.get_mechanical_effects()** (3 connections) — `server/models/profession.py`
- **.set_mechanical_effects()** (3 connections) — `server/models/profession.py`
- **.get_stat_modifiers()** (3 connections) — `server/models/profession.py`
- **.set_stat_modifiers()** (3 connections) — `server/models/profession.py`
- **.get_skill_modifiers()** (3 connections) — `server/models/profession.py`
- **.set_skill_modifiers()** (3 connections) — `server/models/profession.py`
- **.meets_stat_requirements()** (3 connections) — `server/models/profession.py`
- **.get_requirement_display_text()** (3 connections) — `server/models/profession.py`
- **test_get_user_by_username_case_insensitive_database_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_success()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_database_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_os_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_profession_by_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_profession_repr()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_valid_json()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_invalid_json()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_empty_string()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_none()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_set_stat_requirements()** (3 connections) — `server/tests/unit/models/test_profession.py`
- *... and 95 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (10 shared connections)
- [Loot Generation](Loot_Generation.md) (8 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (4 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (1 shared connections)

## Source Files

- `server/models/profession.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_profession.py`

## Audit Trail

- EXTRACTED: 338 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*