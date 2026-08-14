# process_subzone_rows

> 7 nodes

## Key Concepts

- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **test_process_subzone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows_empty()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Connection** (2 connections)
- **Process subzone rows from database and populate subzone configurations. Args:…** (1 connections) — `server/npc/zone_config_loader.py`
- **Test process_subzone_rows() processes subzone rows.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_subzone_rows() handles empty result.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [async_load_zone_configurations](async_load_zone_configurations.md) (5 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (3 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (3 shared connections)
- [process_zone_rows](process_zone_rows.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*