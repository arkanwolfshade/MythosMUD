# _parse_env_list

> 14 nodes

## Key Concepts

- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **_parse_list_from_string()** (4 connections) — `server/config/models/_helpers.py`
- **test_parse_env_list_csv()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_empty_string()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_json()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_none()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_empty_and_none()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_list_from_string_json_and_csv()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **Parse non-empty string as JSON list or CSV. Used by _parse_env_list.** (1 connections) — `server/config/models/_helpers.py`
- **Parse a string from the environment as JSON list or CSV.** (1 connections) — `server/config/models/_helpers.py`
- **Test parsing None as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing empty string as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing JSON list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing CSV list.** (1 connections) — `server/tests/unit/config/test_config_models.py`

## Relationships

- [test_config_models.py](test_config_models.py.md) (6 shared connections)
- [test_config_model_helpers.py](test_config_model_helpers.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*