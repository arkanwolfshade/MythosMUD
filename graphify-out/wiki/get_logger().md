# get_logger()

> God node · 510 connections · `server/structured_logging/enhanced_logging_config.py`

**Community:** [Room Occupancy Class](Room_Occupancy_Class.md)

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
- exceptions.py `EXTRACTED`
- connection_manager.py `EXTRACTED`
- dependencies.py `EXTRACTED`
- combat_service.py `EXTRACTED`
- command_service.py `EXTRACTED`
- time.py `EXTRACTED`
- database.py `EXTRACTED`
- game_tick_processing.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- players.py `EXTRACTED`
- alias_storage.py `EXTRACTED`
- websocket_handler.py `EXTRACTED`
- maps.py `EXTRACTED`
- monitoring.py `EXTRACTED`
- lifespan_startup.py `EXTRACTED`
- character_creation.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- command_handler_unified.py `EXTRACTED`
- connection_manager_methods.py `EXTRACTED`

### rationale_for
- Get a Structlog logger with the specified name.      This ensures all loggers ar `EXTRACTED`

### references
- BoundLogger `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*