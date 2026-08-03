# persistence core infrastructure

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

- [profession models rationale](profession_models_rationale.md) (13 shared connections)
- [Database Config](Database_Config.md) (11 shared connections)
- [player realtime presence](player_realtime_presence.md) (7 shared connections)
- [message handlers realtime](message_handlers_realtime.md) (3 shared connections)
- [room toolkit validator](room_toolkit_validator.md) (2 shared connections)
- [realtime player event](realtime_player_event.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (1 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (1 shared connections)
- [archive LOGGING BEST](archive_LOGGING_BEST.md) (1 shared connections)
- [static schemas room](static_schemas_room.md) (1 shared connections)
- [archive AUDIT EXECUTIVE](archive_AUDIT_EXECUTIVE.md) (1 shared connections)

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