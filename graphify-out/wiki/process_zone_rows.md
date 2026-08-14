# process_zone_rows

> 8 nodes

## Key Concepts

- **process_zone_rows()** (13 connections) — `server/npc/zone_config_loader.py`
- **test_process_zone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_empty()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_json_strings()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Process zone rows from database and populate zone configurations. Args: conn:…** (1 connections) — `server/npc/zone_config_loader.py`
- **Test process_zone_rows() handles empty result.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_zone_rows() parses JSON string fields.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_zone_rows() processes zone rows.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [async_load_zone_configurations](async_load_zone_configurations.md) (7 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (5 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (3 shared connections)
- [extract_zone_name](extract_zone_name.md) (1 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (1 shared connections)
- [process_subzone_rows](process_subzone_rows.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*