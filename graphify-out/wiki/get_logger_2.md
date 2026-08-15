# get_logger()

> God node · 525 connections · `server/structured_logging/enhanced_logging_config.py`

**Community:** [get_logger](get_logger.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- format_metadata() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- handle_new_game_session() `EXTRACTED`
- wrap_third_party_exception_enhanced() `EXTRACTED`
- db_cleanup() `EXTRACTED`
- log_structured_error() `EXTRACTED`
- get_player_connections() `EXTRACTED`
- websocket_endpoint() `EXTRACTED`
- websocket_endpoint_route() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- setup_enhanced_logging() `EXTRACTED`
- get_connection_statistics() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- update_logging_with_player_service() `EXTRACTED`
- _log_http_error() `EXTRACTED`
- .read_token() `EXTRACTED`

### contains
- enhanced_logging_config.py `EXTRACTED`

### imports
- server/exceptions.py `EXTRACTED`
- connection_manager.py `EXTRACTED`
- command_service.py `EXTRACTED`
- [server/dependencies.py](server-dependencies.py.md) `EXTRACTED`
- combat_service.py `EXTRACTED`
- time.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- game_tick_processing.py `EXTRACTED`
- [connection_manager_methods.py](connection_manager_methods.py.md) `EXTRACTED`
- database.py `EXTRACTED`
- [alias_storage.py](alias_storage.py.md) `EXTRACTED`
- players.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- endpoints.py `EXTRACTED`
- [websocket_handler.py](websocket_handler.py.md) `EXTRACTED`
- [api/monitoring.py](api-monitoring.py.md) `EXTRACTED`
- lifespan_startup.py `EXTRACTED`
- [container_endpoints_basic.py](container_endpoints_basic.py.md) `EXTRACTED`
- [chat_service.py](chat_service.py.md) `EXTRACTED`

### rationale_for
- Get a Structlog logger with the specified name. This ensures all loggers are… `EXTRACTED`

### references
- BoundLogger `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*