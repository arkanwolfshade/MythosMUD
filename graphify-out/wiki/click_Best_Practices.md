# click Best Practices

> 20 nodes

## Key Concepts

- **test_config_models.py** (20 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_no_env()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_csv()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_empty_string()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_json()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_none()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_default_host()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_valid()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **Unit tests for configuration models.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test DatabaseConfig pool config validation with positive values.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing None as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing empty string as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing JSON list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing CSV list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test default CORS origins when no env vars set.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test default CORS origins with env var set.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test ServerConfig default host.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test ServerConfig port validation with valid port.** (1 connections) — `server/tests/unit/config/test_config_models.py`

## Relationships

- [.get_combat_stats](get_combat_stats.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [test_get_player_by_name_database_error](test_get_player_by_name_database_error.md) (1 shared connections)
- [zone](zone.md) (1 shared connections)
- [test_process_exit_rows_with_partial_room_ids](test_process_exit_rows_with_partial_room_ids.md) (1 shared connections)
- [test_process_exit_rows_debug_logging](test_process_exit_rows_debug_logging.md) (1 shared connections)
- [test_process_room_rows_with_full_room_id](test_process_room_rows_with_full_room_id.md) (1 shared connections)
- [test_build_room_objects_with_non_dict_attributes](test_build_room_objects_with_non_dict_attributes.md) (1 shared connections)

## Source Files

- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*