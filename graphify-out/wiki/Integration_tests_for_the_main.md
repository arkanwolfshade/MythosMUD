# Integration tests for the main

> 17 nodes

## Key Concepts

- **Profession** (54 connections) — `server/models/profession.py`
- **test_get_professions_success()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_profession_by_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_profession_repr()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_invalid_json()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_set_mechanical_effects()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **.__repr__()** (2 connections) — `server/models/profession.py`
- **.is_available_for_selection()** (2 connections) — `server/models/profession.py`
- **Base** (1 connections)
- **Profession model for game data.      Stores profession information including nam** (1 connections) — `server/models/profession.py`
- **String representation of the profession.** (1 connections) — `server/models/profession.py`
- **Check if profession is available for player selection.** (1 connections) — `server/models/profession.py`
- **Test get_professions with successful query.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **Test get_profession_by_id delegates to ProfessionRepository.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **Test __repr__ returns expected string format.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_stat_requirements returns empty dict for invalid JSON.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test set_mechanical_effects stores dict as JSON string.** (1 connections) — `server/tests/unit/models/test_profession.py`

## Relationships

- [test profession](test_profession.md) (13 shared connections)
- [game](game.md) (7 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (4 shared connections)
- [real time](real_time.md) (4 shared connections)
- [Test build room objects successfully](Test_build_room_objects_successfully.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (1 shared connections)
- [test_normalize_command_removes_slash](test_normalize_command_removes_slash.md) (1 shared connections)
- [test_profession_get_mechanical_effects_valid_json](test_profession_get_mechanical_effects_valid_json.md) (1 shared connections)
- [test_profession_get_requirement_display_text_capitalizes_stat_names](test_profession_get_requirement_display_text_capitalizes_stat_names.md) (1 shared connections)
- [test_profession_get_requirement_display_text_no_requirements](test_profession_get_requirement_display_text_no_requirements.md) (1 shared connections)

## Source Files

- `server/models/profession.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_profession.py`

## Audit Trail

- EXTRACTED: 75 (91%)
- INFERRED: 7 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*