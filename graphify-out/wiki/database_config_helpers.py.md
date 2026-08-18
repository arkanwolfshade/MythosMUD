# database_config_helpers.py

> 89 nodes

## Key Concepts

- **database_config_helpers.py** (25 connections) — `server/database_config_helpers.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **rate_overrides.py** (19 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **_process_override_row()** (11 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_database_config_helpers_asyncpg_settings.py** (10 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **_async_load_lucidity_rate_overrides()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **configure_pool_settings()** (5 connections) — `server/database_config_helpers.py`
- **.get_session_maker()** (5 connections) — `server/database.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **normalize_environment_config()** (5 connections) — `server/services/passive_lucidity_flux/config.py`
- **build_override_key()** (5 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **_LucidityRateLoadResult** (4 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **.get_engine()** (4 connections) — `server/database.py`
- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **load_lucidity_rate_overrides()** (4 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **clear_postgres_search_path()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- *... and 64 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (25 shared connections)
- [get_logger](get_logger.md) (19 shared connections)
- [DatabaseManager](DatabaseManager.md) (10 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [EmoteService](EmoteService.md) (2 shared connections)
- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (2 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (2 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [_schedule_entry_from_row](_schedule_entry_from_row.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/game/emote_service.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 204 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*