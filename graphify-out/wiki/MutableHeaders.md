# MutableHeaders

> 8 nodes

## Key Concepts

- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **test_load_zone_configurations_success()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_merges_zone_and_subzone()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_error()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Load zone and sub-zone configurations from PostgreSQL database.      Returns:** (1 connections) — `server/npc/zone_config_loader.py`
- **Test load_zone_configurations() loads configurations.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test load_zone_configurations() merges zone and subzone configs.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test load_zone_configurations() raises RuntimeError on failure.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [HealthMonitor](HealthMonitor.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [memory lifespan coordinator](memory_lifespan_coordinator.md) (1 shared connections)
- [Represents the configuration for a](Represents_the_configuration_for_a.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*