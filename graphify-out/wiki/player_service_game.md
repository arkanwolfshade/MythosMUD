# player service game

> 28 nodes

## Key Concepts

- **factory.py** (45 connections) — `server/app/factory.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **_register_v1_routers()** (7 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **UserRead** (6 connections) — `server/auth/endpoints.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **_first_set_env()** (3 connections) — `server/app/factory.py`
- **_try_json_str_list()** (3 connections) — `server/app/factory.py`
- **FastAPI** (3 connections)
- **TypedDict** (2 connections)
- **FastAPI application factory for MythosMUD server.  This module handles FastAPI a** (1 connections) — `server/app/factory.py`
- **Type definition for CORS configuration dictionary.** (1 connections) — `server/app/factory.py`
- **Partial CORS overrides from environment variables.** (1 connections) — `server/app/factory.py`
- **Get default CORS configuration values.      Returns:         CORSConfigDict: Dic** (1 connections) — `server/app/factory.py`
- **Get CORS configuration from AppConfig, with fallback to defaults.      Returns:** (1 connections) — `server/app/factory.py`
- **Return the first non-empty environment value among keys.** (1 connections) — `server/app/factory.py`
- **Parse candidate as a JSON string list, or None on failure.** (1 connections) — `server/app/factory.py`
- **Parse CORS origins env value as JSON array or comma-separated list.** (1 connections) — `server/app/factory.py`
- **Parse CORS-related environment variables and return overrides.      Environment** (1 connections) — `server/app/factory.py`
- **Merge environment CORS overrides into the full config in place.** (1 connections) — `server/app/factory.py`
- *... and 3 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (8 shared connections)
- [npc combat services](npc_combat_services.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [command combat models](command_combat_models.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [auth users rationale](auth_users_rationale.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [config models cors](config_models_cors.md) (2 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (2 shared connections)
- [middleware error handling](middleware_error_handling.md) (2 shared connections)
- [persistence rationale player](persistence_rationale_player.md) (2 shared connections)

## Source Files

- `server/app/factory.py`
- `server/auth/endpoints.py`

## Audit Trail

- EXTRACTED: 118 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*