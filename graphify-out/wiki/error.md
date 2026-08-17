# .error

> 18 nodes

## Key Concepts

- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **Build legacy dict entries for game config.** (1 connections) — `server/config/models/app.py`
- **Build legacy nats nested dict.** (1 connections) — `server/config/models/app.py`
- **Build legacy chat nested dict.** (1 connections) — `server/config/models/app.py`
- **Build legacy cors nested dict.** (1 connections) — `server/config/models/app.py`
- **Initialize configuration and set environment variables for legacy compatibility.** (1 connections) — `server/config/models/app.py`
- **Return first set CORS origins env var to reduce CCN in _sanitize.** (1 connections) — `server/config/models/app.py`
- **Normalize environment variables so nested configs can parse them reliably.** (1 connections) — `server/config/models/app.py`
- **Convert to legacy dict format for backward compatibility. This allows gradual…** (1 connections) — `server/config/models/app.py`

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [datetime](datetime.md) (2 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (2 shared connections)
- [CORSConfig](CORSConfig.md) (1 shared connections)
- [GameConfig](GameConfig.md) (1 shared connections)
- [NATSConfig](NATSConfig.md) (1 shared connections)
- [test_lifespan_helpers.py](test_lifespan_helpers.py.md) (1 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (1 shared connections)

## Source Files

- `server/config/models/app.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 33 (82%)
- INFERRED: 7 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*