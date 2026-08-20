# CORSConfigDict

> 21 nodes

## Key Concepts

- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **_first_set_env()** (3 connections) — `server/app/factory.py`
- **_try_json_str_list()** (3 connections) — `server/app/factory.py`
- **TypedDict** (2 connections)
- **Get CORS configuration from AppConfig, with fallback to defaults. Returns:…** (1 connections) — `server/app/factory.py`
- **Return the first non-empty environment value among keys.** (1 connections) — `server/app/factory.py`
- **Parse candidate as a JSON string list, or None on failure.** (1 connections) — `server/app/factory.py`
- **Parse CORS origins env value as JSON array or comma-separated list.** (1 connections) — `server/app/factory.py`
- **Parse CORS-related environment variables and return overrides. Environment…** (1 connections) — `server/app/factory.py`
- **Merge environment CORS overrides into the full config in place.** (1 connections) — `server/app/factory.py`
- **Configure CORS settings from config file and environment variables. Precedence:…** (1 connections) — `server/app/factory.py`
- **Type definition for CORS configuration dictionary.** (1 connections) — `server/app/factory.py`
- **Partial CORS overrides from environment variables.** (1 connections) — `server/app/factory.py`
- **Get default CORS configuration values. Returns: CORSConfigDict: Dictionary with…** (1 connections) — `server/app/factory.py`

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [server/main.py](server-main.py.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/app/factory.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*