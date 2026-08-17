# database_config_helpers.py

> 76 nodes

## Key Concepts

- **database_config_helpers.py** (25 connections) — `server/database_config_helpers.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **rate_overrides.py** (19 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **_process_override_row()** (11 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_database_config_helpers_asyncpg_settings.py** (10 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **validate_database_url()** (6 connections) — `server/database_config_helpers.py`
- **_async_load_lucidity_rate_overrides()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **configure_pool_settings()** (5 connections) — `server/database_config_helpers.py`
- **.get_session_maker()** (5 connections) — `server/database.py`
- **build_override_key()** (5 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **_LucidityRateLoadResult** (4 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_normalize_connect_args_search_path()** (4 connections) — `server/database.py`
- **clear_postgres_search_path()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_mythos_unit_defaults_search_path_to_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_respects_postgres_search_path_when_matches_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_empty_when_no_env()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_uses_postgres_search_path_when_set()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- *... and 51 more nodes in this community*

## Relationships

- [get_session_maker](get_session_maker.md) (12 shared connections)
- [DatabaseManager](DatabaseManager.md) (9 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [npc_database.py](npc_database.py.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [service.py](service.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [emote_service.py](emote_service.py.md) (3 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (3 shared connections)
- [HolidayService](HolidayService.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 173 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*