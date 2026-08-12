# get_logger()

> God node · 509 connections · `server/structured_logging/enhanced_logging_config.py`

**Community:** [get_logger](get_logger.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- format_metadata() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- db_cleanup() `EXTRACTED`
- websocket_endpoint() `EXTRACTED`
- wrap_third_party_exception_enhanced() `EXTRACTED`
- get_player_connections() `EXTRACTED`
- handle_new_game_session() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- setup_enhanced_logging() `EXTRACTED`
- log_structured_error() `EXTRACTED`
- websocket_endpoint_route() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- update_logging_with_player_service() `EXTRACTED`
- _log_http_error() `EXTRACTED`
- get_connection_statistics() `EXTRACTED`
- .read_token() `EXTRACTED`

### contains
- enhanced_logging_config.py `EXTRACTED`

### imports
- [server/exceptions.py](server-exceptions.py.md) `EXTRACTED`
- [connection_manager.py](connection_manager.py.md) `EXTRACTED`
- [server/dependencies.py](server-dependencies.py.md) `EXTRACTED`
- [combat_service.py](combat_service.py.md) `EXTRACTED`
- command_service.py `EXTRACTED`
- [time.py](time.py.md) `EXTRACTED`
- [game_tick_processing.py](game_tick_processing.py.md) `EXTRACTED`
- database.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- players.py `EXTRACTED`
- [alias_storage.py](alias_storage.py.md) `EXTRACTED`
- [websocket_handler.py](websocket_handler.py.md) `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- [api/monitoring.py](api-monitoring.py.md) `EXTRACTED`
- [lifespan_startup.py](lifespan_startup.py.md) `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- persistence/container_persistence.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- connection_manager_methods.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`

### rationale_for
- Get a Structlog logger with the specified name. This ensures all loggers are… `EXTRACTED`

### references
- BoundLogger `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*