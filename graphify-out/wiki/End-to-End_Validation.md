# End-to-End Validation

> 27 nodes

## Key Concepts

- **service.py** (31 connections) — `server/services/passive_lucidity_flux/service.py`
- **config.py** (11 connections) — `server/services/passive_lucidity_flux/config.py`
- **PassiveFluxContext** (10 connections) — `server/services/passive_lucidity_flux/models.py`
- **PlayerFluxCtx** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **FluxServiceConfig** (7 connections) — `server/services/passive_lucidity_flux/config.py`
- **CachedRoom** (7 connections) — `server/services/passive_lucidity_flux/models.py`
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **period_label()** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **models.py** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **__init__.py** (5 connections) — `server/services/passive_lucidity_flux/__init__.py`
- **normalize_environment_config()** (5 connections) — `server/services/passive_lucidity_flux/config.py`
- **lookup_profile()** (4 connections) — `server/services/passive_lucidity_flux/config.py`
- **load_lucidity_rate_overrides()** (4 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **datetime** (2 connections)
- **Passive lucidity flux service package.** (1 connections) — `server/services/passive_lucidity_flux/__init__.py`
- **Any** (1 connections)
- **Configuration and normalization for passive lucidity flux.** (1 connections) — `server/services/passive_lucidity_flux/config.py`
- **Optional configuration for PassiveLucidityFluxService. All fields have defaults.** (1 connections) — `server/services/passive_lucidity_flux/config.py`
- **Return a coarse period label used for environment profiles.** (1 connections) — `server/services/passive_lucidity_flux/config.py`
- **Normalize environment config to validated structure.** (1 connections) — `server/services/passive_lucidity_flux/config.py`
- **Look up flux value from profile by period.** (1 connections) — `server/services/passive_lucidity_flux/config.py`
- **Data models for passive lucidity flux.** (1 connections) — `server/services/passive_lucidity_flux/models.py`
- **Cached room entry with timestamp for TTL management.** (1 connections) — `server/services/passive_lucidity_flux/models.py`
- **Resolved environmental context for passive flux evaluation.** (1 connections) — `server/services/passive_lucidity_flux/models.py`
- **Load lucidity rate overrides from PostgreSQL zones/subzones tables.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- *... and 2 more nodes in this community*

## Relationships

- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (14 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (5 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (4 shared connections)
- [Test Migration Report](Test_Migration_Report.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (2 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Cursor Plans Postgresql](Cursor_Plans_Postgresql.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 114 (90%)
- INFERRED: 13 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*