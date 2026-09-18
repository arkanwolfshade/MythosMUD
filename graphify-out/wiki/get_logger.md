# get_logger()

> God node · 542 connections · `server/structured_logging/enhanced_logging_config.py`

**Community:** [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- format_metadata() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- handle_new_game_session() `EXTRACTED`
- wrap_third_party_exception_enhanced() `EXTRACTED`
- setup_enhanced_logging() `EXTRACTED`
- db_cleanup() `EXTRACTED`
- log_structured_error() `EXTRACTED`
- get_player_connections() `EXTRACTED`
- websocket_endpoint() `EXTRACTED`
- websocket_endpoint_route() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- get_connection_statistics() `EXTRACTED`
- .__init__() `EXTRACTED`
- _log_http_error() `EXTRACTED`
- .read_token() `EXTRACTED`
- .__init__() `EXTRACTED`
- update_logging_with_player_service() `EXTRACTED`

### contains
- enhanced_logging_config.py `EXTRACTED`

### imports
- server/exceptions.py `EXTRACTED`
- time.py `EXTRACTED`
- combat_service.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- server/dependencies.py `EXTRACTED`
- database.py `EXTRACTED`
- connection_manager.py `EXTRACTED`
- alias_storage.py `EXTRACTED`
- players.py `EXTRACTED`
- websocket_handler.py `EXTRACTED`
- connection_manager_methods.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- maps.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- chat_service.py `EXTRACTED`
- api/monitoring.py `EXTRACTED`
- rooms.py `EXTRACTED`
- models/combat.py `EXTRACTED`
- look_command.py `EXTRACTED`

### rationale_for
- Get a Structlog logger with the specified name. This ensures all loggers are… `EXTRACTED`

### references
- BoundLogger `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*