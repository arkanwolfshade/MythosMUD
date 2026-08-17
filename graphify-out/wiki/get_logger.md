# get_logger()

> God node · 503 connections · `server/structured_logging/enhanced_logging_config.py`

**Community:** [claude rules asyncio](claude_rules_asyncio.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- format_metadata() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- handle_new_game_session() `EXTRACTED`
- wrap_third_party_exception_enhanced() `EXTRACTED`
- websocket_endpoint() `EXTRACTED`
- db_cleanup() `EXTRACTED`
- log_structured_error() `EXTRACTED`
- get_player_connections() `EXTRACTED`
- websocket_endpoint_route() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- setup_enhanced_logging() `EXTRACTED`
- get_connection_statistics() `EXTRACTED`
- .__init__() `EXTRACTED`
- update_logging_with_player_service() `EXTRACTED`
- _log_http_error() `EXTRACTED`
- .read_token() `EXTRACTED`
- .__init__() `EXTRACTED`

### contains
- enhanced_logging_config.py `EXTRACTED`

### imports
- server/exceptions.py `EXTRACTED`
- command_service.py `EXTRACTED`
- server/dependencies.py `EXTRACTED`
- combat_service.py `EXTRACTED`
- time.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- database.py `EXTRACTED`
- alias_storage.py `EXTRACTED`
- players.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- maps.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- websocket_handler.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- api/monitoring.py `EXTRACTED`
- lifespan_startup.py `EXTRACTED`
- chat_service.py `EXTRACTED`
- models/combat.py `EXTRACTED`
- command_handler_unified.py `EXTRACTED`
- persistence/container_persistence.py `EXTRACTED`

### rationale_for
- Get a Structlog logger with the specified name. This ensures all loggers are… `EXTRACTED`

### references
- BoundLogger `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*