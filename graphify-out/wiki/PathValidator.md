# PathValidator

> 61 nodes · cohesion 0.05

## Key Concepts

- **PathValidator** (25 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **validator.py** (15 connections) — `tools/room_toolkit/room_validator/validator.py`
- **__init__.py** (11 connections) — `tools/room_toolkit/room_validator/core/__init__.py`
- **main()** (10 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_initialize_validator_components()** (8 connections) — `tools/room_toolkit/room_validator/validator.py`
- **Any** (7 connections)
- **.check_bidirectional_connections()** (6 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **_apply_automatic_fixes()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_generate_minimap()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_load_and_filter_rooms()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_report_results()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_validate_config_files()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_validate_room_connectivity()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **.build_graph()** (5 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_exit_target()** (5 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **reporter.py** (5 connections) — `tools/room_toolkit/room_validator/core/reporter.py`
- **room_loader.py** (5 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **_collect_parsing_errors()** (5 connections) — `tools/room_toolkit/room_validator/validator.py`
- **fixer.py** (4 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **path_validator.py** (4 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **minimap_renderer.py** (3 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **.find_dead_ends()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.find_self_references()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.generate_minimap_graph()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_opposite_direction()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- *... and 36 more nodes in this community*

## Relationships

- [RoomLoader](RoomLoader.md) (8 shared connections)
- [Reporter](Reporter.md) (7 shared connections)
- [SchemaValidator](SchemaValidator.md) (6 shared connections)
- [RoomFixer](RoomFixer.md) (4 shared connections)
- [TestValidatorIntegration](TestValidatorIntegration.md) (3 shared connections)
- [MinimapRenderer](MinimapRenderer.md) (2 shared connections)
- [TestPathValidator](TestPathValidator.md) (2 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/__init__.py`
- `tools/room_toolkit/room_validator/core/fixer.py`
- `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- `tools/room_toolkit/room_validator/core/path_validator.py`
- `tools/room_toolkit/room_validator/core/reporter.py`
- `tools/room_toolkit/room_validator/core/room_loader.py`
- `tools/room_toolkit/room_validator/tests/test_reporter.py`
- `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- `tools/room_toolkit/room_validator/validator.py`

## Audit Trail

- EXTRACTED: 205 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*