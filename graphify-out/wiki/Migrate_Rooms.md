# Migrate Rooms

> 24 nodes · cohesion 0.12

## Key Concepts

- **migrate_rooms.py** (12 connections) — `scripts/migrate_rooms.py`
- **migrate_rooms()** (10 connections) — `scripts/migrate_rooms.py`
- **_create_subzone_structure()** (4 connections) — `scripts/migrate_rooms.py`
- **_create_zone_structure()** (4 connections) — `scripts/migrate_rooms.py`
- **_load_and_validate_rooms()** (4 connections) — `scripts/migrate_rooms.py`
- **_create_backup()** (3 connections) — `scripts/migrate_rooms.py`
- **create_subzone_config()** (3 connections) — `scripts/migrate_rooms.py`
- **create_zone_config()** (3 connections) — `scripts/migrate_rooms.py`
- **determine_zone_type()** (3 connections) — `scripts/migrate_rooms.py`
- **load_existing_rooms()** (3 connections) — `scripts/migrate_rooms.py`
- **main()** (3 connections) — `scripts/migrate_rooms.py`
- **_migrate_room_file()** (3 connections) — `scripts/migrate_rooms.py`
- **_group_rooms_by_zone()** (2 connections) — `scripts/migrate_rooms.py`
- **Determine the zone type based on the zone name.      Args:         zone_name: Na** (1 connections) — `scripts/migrate_rooms.py`
- **Load existing rooms and validate.** (1 connections) — `scripts/migrate_rooms.py`
- **Create backup if requested.** (1 connections) — `scripts/migrate_rooms.py`
- **Create zone directory and config. Returns zone_path.** (1 connections) — `scripts/migrate_rooms.py`
- **Create sub-zone directory and config. Returns subzone_path.** (1 connections) — `scripts/migrate_rooms.py`
- **Load all existing room files from the flat structure.      Args:         rooms_p** (1 connections) — `scripts/migrate_rooms.py`
- **Migrate a single room file.** (1 connections) — `scripts/migrate_rooms.py`
- **Migrate existing rooms to the new hierarchical structure.      Args:         roo** (1 connections) — `scripts/migrate_rooms.py`
- **Main entry point for the migration script.** (1 connections) — `scripts/migrate_rooms.py`
- **Create a default zone configuration.      Args:         zone_name: Name of the z** (1 connections) — `scripts/migrate_rooms.py`
- **Create a default sub-zone configuration.      Args:         subzone_name: Name o** (1 connections) — `scripts/migrate_rooms.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/migrate_rooms.py`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
