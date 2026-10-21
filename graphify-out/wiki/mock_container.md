# mock_container

> 9 nodes · cohesion 0.25

## Key Concepts

- **ascii_map_renderer.py** (16 connections) — `server/services/ascii_map_renderer.py`
- **test_ascii_map_symbols.py** (6 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **TestRendererBinding** (4 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **ascii_map_symbols.py** (3 connections) — `server/services/ascii_map_symbols.py`
- **.test_renderer_exposes_the_moved_tables()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **ASCII map renderer for MythosMUD. This module provides server-side rendering of…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Symbol and colour tables for the ASCII map. Pure configuration, split out of…** (1 connections) — `server/services/ascii_map_symbols.py`
- **Guards the symbol tables split out of `ascii_map_renderer.py` (#829). The…** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **`renderer.symbols` and friends must still resolve to the moved tables.** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`

## Relationships

- [RoomDataValidator](RoomDataValidator.md) (4 shared connections)
- [Room](Room.md) (2 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (2 shared connections)
- [ItemCatalogService](ItemCatalogService.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [NATS Complete Remediation Summary](NATS_Complete_Remediation_Summary.md) (1 shared connections)
- [Migration Strategy](Migration_Strategy.md) (1 shared connections)
- [ClientLogger](ClientLogger.md) (1 shared connections)
- [field_validator](field_validator.md) (1 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (1 shared connections)
- [required](required.md) (1 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`
- `server/services/ascii_map_symbols.py`
- `server/tests/unit/services/test_ascii_map_symbols.py`

## Audit Trail

- EXTRACTED: 25 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*