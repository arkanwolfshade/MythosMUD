# _default_cors_origins

> 7 nodes

## Key Concepts

- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **test_default_cors_origins_no_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_fallback()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **Derive default CORS origins with environment taking precedence.** (1 connections) — `server/config/models/_helpers.py`
- **Test default CORS origins when no env vars set.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test default CORS origins with env var set.** (1 connections) — `server/tests/unit/config/test_config_models.py`

## Relationships

- [test_config_models.py](test_config_models.py.md) (3 shared connections)
- [test_config_model_helpers.py](test_config_model_helpers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [_parse_env_list](_parse_env_list.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*