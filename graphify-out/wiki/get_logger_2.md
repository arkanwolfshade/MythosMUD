# get_logger()

> God node · 530 connections · `server/structured_logging/enhanced_logging_config.py`

**Community:** [generate_invites_db.py](generate_invites_db.py.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- format_metadata() `EXTRACTED`
- .__init__() `EXTRACTED`
- handle_new_game_session() `EXTRACTED`
- db_cleanup() `EXTRACTED`
- .__init__() `EXTRACTED`
- wrap_third_party_exception_enhanced() `EXTRACTED`
- get_player_connections() `EXTRACTED`
- websocket_endpoint() `EXTRACTED`
- websocket_endpoint_route() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- log_structured_error() `EXTRACTED`
- get_connection_statistics() `EXTRACTED`
- .__init__() `EXTRACTED`
- setup_enhanced_logging() `EXTRACTED`
- .read_token() `EXTRACTED`
- .__init__() `EXTRACTED`
- _log_http_error() `EXTRACTED`
- .__init__() `EXTRACTED`

### contains
- enhanced_logging_config.py `EXTRACTED`

### imports
- server/exceptions.py `EXTRACTED`
- [command_service.py](command_service.py.md) `EXTRACTED`
- [server/dependencies.py](server-dependencies.py.md) `EXTRACTED`
- time.py `EXTRACTED`
- [connection_manager_methods.py](connection_manager_methods.py.md) `EXTRACTED`
- database.py `EXTRACTED`
- [connection_manager.py](connection_manager.py.md) `EXTRACTED`
- alias_storage.py `EXTRACTED`
- combat_service.py `EXTRACTED`
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- [container_endpoints_basic.py](container_endpoints_basic.py.md) `EXTRACTED`
- async_persistence.py `EXTRACTED`
- [websocket_handler.py](websocket_handler.py.md) `EXTRACTED`
- models/combat.py `EXTRACTED`
- rooms.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- factory.py `EXTRACTED`

### rationale_for
- Get a Structlog logger with the specified name. This ensures all loggers are… `EXTRACTED`

### references
- BoundLogger `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*