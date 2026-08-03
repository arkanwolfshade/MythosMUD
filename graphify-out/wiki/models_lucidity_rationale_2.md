# models lucidity rationale

> 10 nodes

## Key Concepts

- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **test_extract_zone_name_with_slash()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_no_slash()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_multiple_slashes()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_empty()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Extract zone name from stable_id (format: 'plane/zone').      Args:         stab** (1 connections) — `server/npc/zone_config_loader.py`
- **Test extract_zone_name() extracts zone from stable_id.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test extract_zone_name() returns stable_id when no slash.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test extract_zone_name() extracts from first slash.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test extract_zone_name() handles empty string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [npc realtime occupant](npc_realtime_occupant.md) (6 shared connections)
- [npc idle movement](npc_idle_movement.md) (2 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*