# server services passive lucidity flux

> 22 nodes

## Key Concepts

- **rate_overrides.py** (19 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_process_override_row()** (11 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_async_load_lucidity_rate_overrides()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **build_override_key()** (5 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_LucidityRateLoadResult** (4 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **extract_lucidity_rate()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_normalize_database_url()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_parse_special_rules_from_raw()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_parse_zone_stable_id()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **rate_to_flux()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_warn_if_rate_exceeds_threshold()** (2 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Record** (1 connections)
- **TypedDict** (1 connections)
- **Load lucidity rate overrides from PostgreSQL zones/subzones.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Process a single zone/subzone row and add override to result_container if valid.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Async helper to load lucidity rate overrides from PostgreSQL.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Build override key from plane/zone/subzone hierarchy.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Convert lucidity_drain_rate to flux value. Args: rate: Lucidity drain rate…** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Extract lucidity_drain_rate from special_rules config.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Convert SQLAlchemy-style URL to asyncpg-compatible format.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Parse plane and zone from zone_stable_id (format: 'plane/zone').** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Parse special_rules column value into a dict.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`

## Relationships

- [passivelucidityfluxservice](passivelucidityfluxservice.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/rate_overrides.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*