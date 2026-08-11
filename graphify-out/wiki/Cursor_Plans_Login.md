# Cursor Plans Login

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

- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (13 shared connections)
- [E 2 E Cleanup Troubleshooting](E_2_E_Cleanup_Troubleshooting.md) (7 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (5 shared connections)
- [Archive Planning Unified](Archive_Planning_Unified.md) (3 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Troubleshooting Guide](Troubleshooting_Guide.md) (1 shared connections)
- [test_process_room_rows_with_none_stable_id](test_process_room_rows_with_none_stable_id.md) (1 shared connections)
- [test_process_combined_rows_with_exits](test_process_combined_rows_with_exits.md) (1 shared connections)
- [test_process_exits_for_room_no_direction](test_process_exits_for_room_no_direction.md) (1 shared connections)

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