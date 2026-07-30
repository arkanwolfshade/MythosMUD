# datetime

> 7 nodes

## Key Concepts

- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **test_process_subzone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows_empty()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Connection** (2 connections)
- **Process subzone rows from database and populate subzone configurations.      Arg** (1 connections) — `server/npc/zone_config_loader.py`
- **Test process_subzone_rows() processes subzone rows.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_subzone_rows() handles empty result.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [HealthMonitor](HealthMonitor.md) (4 shared connections)
- [memory lifespan coordinator](memory_lifespan_coordinator.md) (3 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (3 shared connections)
- [Represents the configuration for a](Represents_the_configuration_for_a.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*