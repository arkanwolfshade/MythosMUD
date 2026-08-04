# realtime dead letter

> 9 nodes

## Key Concepts

- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **Request** (5 connections)
- **Enhanced health check endpoint using monitoring dashboard.** (1 connections) — `server/api/system_monitoring.py`
- **Get system alerts from monitoring dashboard.** (1 connections) — `server/api/system_monitoring.py`
- **Resolve a system alert.** (1 connections) — `server/api/system_monitoring.py`
- **Unit tests for main.py monitoring endpoints and lifespan functions.  Tests monit** (1 connections) — `server/tests/unit/test_main.py`

## Relationships

- [command combat models](command_combat_models.md) (10 shared connections)
- [System Metrics](System_Metrics.md) (8 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (6 shared connections)
- [Exception Containers](Exception_Containers.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*