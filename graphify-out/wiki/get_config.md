# get_config

> 148 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **factory.py** (37 connections) — `server/app/factory.py`
- **server/main.py** (15 connections) — `server/main.py`
- **SecurityHeadersMiddleware** (12 connections) — `server/middleware/security_headers.py`
- **ConnectionErrorHandler** (12 connections) — `server/realtime/errors/error_handler.py`
- **create_app()** (11 connections) — `server/app/factory.py`
- **server/config/__init__.py** (11 connections) — `server/config/__init__.py`
- **ComprehensiveLoggingMiddleware** (9 connections) — `server/middleware/comprehensive_logging.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **correlation_middleware.py** (9 connections) — `server/middleware/correlation_middleware.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **.detect_and_handle_error_state()** (8 connections) — `server/realtime/errors/error_handler.py`
- **load_motd()** (8 connections) — `server/utils/motd_loader.py`
- **UUID** (8 connections)
- **Any** (7 connections)
- **test_motd_loader.py** (7 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **.delete_player()** (6 connections) — `server/game/player_service.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- *... and 123 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (33 shared connections)
- [CombatService](CombatService.md) (14 shared connections)
- [.__call__](__call__.md) (8 shared connections)
- [AppConfig](AppConfig.md) (7 shared connections)
- [.get_instance](get_instance.md) (6 shared connections)
- [test_security_headers.py](test_security_headers.py.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [User](User.md) (4 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `scripts/verify_and_load_seed.py`
- `server/app/factory.py`
- `server/config/__init__.py`
- `server/game/player_service.py`
- `server/main.py`
- `server/middleware/comprehensive_logging.py`
- `server/middleware/correlation_middleware.py`
- `server/middleware/security_headers.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `server/tests/unit/utils/test_motd_loader.py`
- `server/time/time_service.py`
- `server/utils/motd_loader.py`

## Audit Trail

- EXTRACTED: 362 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*