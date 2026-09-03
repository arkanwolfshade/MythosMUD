# get_logger()

> God node · 463 connections · `server/structured_logging/enhanced_logging_config.py`

**Community:** [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- format_metadata() `EXTRACTED`
- .__init__() `EXTRACTED`
- wrap_third_party_exception_enhanced() `EXTRACTED`
- db_cleanup() `EXTRACTED`
- log_structured_error() `EXTRACTED`
- .__init__() `EXTRACTED`
- update_logging_with_player_service() `EXTRACTED`
- _log_http_error() `EXTRACTED`
- .read_token() `EXTRACTED`
- setup_enhanced_logging() `EXTRACTED`
- .__init__() `EXTRACTED`
- log_performance_metric() `EXTRACTED`
- log_security_event_enhanced() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### contains
- enhanced_logging_config.py `EXTRACTED`

### imports
- server/exceptions.py `EXTRACTED`
- connection_manager.py `EXTRACTED`
- server/dependencies.py `EXTRACTED`
- time.py `EXTRACTED`
- combat_service.py `EXTRACTED`
- connection_manager_methods.py `EXTRACTED`
- alias_storage.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- lifespan_startup.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- api/monitoring.py `EXTRACTED`
- chat_service.py `EXTRACTED`
- models/combat.py `EXTRACTED`
- look_command.py `EXTRACTED`
- game_tick_processing.py `EXTRACTED`
- factory.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- lucidity_service.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`

### rationale_for
- Get a Structlog logger with the specified name. This ensures all loggers are… `EXTRACTED`

### references
- BoundLogger `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*