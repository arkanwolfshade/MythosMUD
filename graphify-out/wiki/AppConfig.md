# AppConfig

> 23 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **.set_legacy_environment_variables()** (3 connections) — `server/config/models/app.py`
- **BaseSettings** (1 connections)
- **model_validator** (1 connections)
- **Build legacy dict entries for game config.** (1 connections) — `server/config/models/app.py`
- **Build legacy nats nested dict.** (1 connections) — `server/config/models/app.py`
- **Build legacy chat nested dict.** (1 connections) — `server/config/models/app.py`
- **Build legacy cors nested dict.** (1 connections) — `server/config/models/app.py`
- **Composite application configuration. This is the main configuration class that…** (1 connections) — `server/config/models/app.py`
- **Initialize configuration and set environment variables for legacy compatibility.** (1 connections) — `server/config/models/app.py`
- **Set environment variables for legacy code that reads them directly.** (1 connections) — `server/config/models/app.py`
- **Return first set CORS origins env var to reduce CCN in _sanitize.** (1 connections) — `server/config/models/app.py`
- **Normalize environment variables so nested configs can parse them reliably.** (1 connections) — `server/config/models/app.py`
- **Convert to legacy dict format for backward compatibility. This allows gradual…** (1 connections) — `server/config/models/app.py`

## Relationships

- [config/models/__init__.py](config-models-__init__.py.md) (5 shared connections)
- [server/config/__init__.py](server-config-__init__.py.md) (4 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (3 shared connections)
- [test_config_models.py](test_config_models.py.md) (2 shared connections)
- [NATSConfig](NATSConfig.md) (2 shared connections)
- [LoggingConfig](LoggingConfig.md) (2 shared connections)
- [GameConfig](GameConfig.md) (2 shared connections)
- [CORSConfig](CORSConfig.md) (2 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [PlayerStatsConfig](PlayerStatsConfig.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)

## Source Files

- `server/config/models/app.py`

## Audit Trail

- EXTRACTED: 47 (81%)
- INFERRED: 11 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*