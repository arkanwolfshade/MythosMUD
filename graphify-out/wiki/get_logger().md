# get_logger()

> God node · 506 connections · `server/structured_logging/enhanced_logging_config.py`

**Community:** [get_logger](get_logger.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- .__init__() `EXTRACTED`
- format_metadata() `EXTRACTED`
- .__init__() `EXTRACTED`
- configure_enhanced_structlog() `EXTRACTED`
- websocket_endpoint() `EXTRACTED`
- .__init__() `EXTRACTED`
- db_cleanup() `EXTRACTED`
- wrap_third_party_exception_enhanced() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- setup_enhanced_logging() `EXTRACTED`
- log_structured_error() `EXTRACTED`
- get_player_connections() `EXTRACTED`
- handle_new_game_session() `EXTRACTED`
- websocket_endpoint_route() `EXTRACTED`
- .__init__() `EXTRACTED`
- update_logging_with_player_service() `EXTRACTED`
- _log_http_error() `EXTRACTED`
- .read_token() `EXTRACTED`

### contains
- enhanced_logging_config.py `EXTRACTED`

### imports
- [exceptions.py](exceptions.py.md) `EXTRACTED`
- [connection_manager.py](connection_manager.py.md) `EXTRACTED`
- [dependencies.py](dependencies.py.md) `EXTRACTED`
- combat_service.py `EXTRACTED`
- command_service.py `EXTRACTED`
- time.py `EXTRACTED`
- connection_manager_methods.py `EXTRACTED`
- database.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- [game_tick_processing.py](game_tick_processing.py.md) `EXTRACTED`
- players.py `EXTRACTED`
- alias_storage.py `EXTRACTED`
- [websocket_handler.py](websocket_handler.py.md) `EXTRACTED`
- [monitoring.py](monitoring.py.md) `EXTRACTED`
- lifespan_startup.py `EXTRACTED`
- [container_persistence.py](container_persistence.py.md) `EXTRACTED`
- maps.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- [command_handler_unified.py](command_handler_unified.py.md) `EXTRACTED`
- [container_endpoints_basic.py](container_endpoints_basic.py.md) `EXTRACTED`

### rationale_for
- Get a Structlog logger with the specified name.      This ensures all loggers ar `EXTRACTED`

### references
- BoundLogger `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*