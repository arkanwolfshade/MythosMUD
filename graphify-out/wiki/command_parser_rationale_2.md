# command parser rationale

> 26 nodes

## Key Concepts

- **service.py** (30 connections) — `server/services/passive_lucidity_flux/service.py`
- **PassiveFluxContext** (13 connections) — `server/services/passive_lucidity_flux/models.py`
- **config.py** (12 connections) — `server/services/passive_lucidity_flux/config.py`
- **FluxServiceConfig** (9 connections) — `server/services/passive_lucidity_flux/config.py`
- **models.py** (7 connections) — `server/services/passive_lucidity_flux/models.py`
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **__init__.py** (6 connections) — `server/services/passive_lucidity_flux/__init__.py`
- **period_label()** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **CachedRoom** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **normalize_environment_config()** (5 connections) — `server/services/passive_lucidity_flux/config.py`
- **lookup_profile()** (4 connections) — `server/services/passive_lucidity_flux/config.py`
- **load_lucidity_rate_overrides()** (4 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_resolve_context_with_custom_resolver()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
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
- *... and 1 more nodes in this community*

## Relationships

- [lucidity flux passive](lucidity_flux_passive.md) (14 shared connections)
- [cache lru caching](cache_lru_caching.md) (8 shared connections)
- [player room realtime](player_room_realtime.md) (6 shared connections)
- [rate lucidity services](rate_lucidity_services.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)
- [npc population stats](npc_population_stats.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [Spell Validation](Spell_Validation.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/tests/unit/services/test_passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 122 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*