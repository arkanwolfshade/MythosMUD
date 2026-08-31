# lifespan_startup.py

> 121 nodes

## Key Concepts

- **lifespan_startup.py** (66 connections) — `server/app/lifespan_startup.py`
- **lifespan.py** (46 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (27 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (16 connections) — `server/app/lifespan.py`
- **FastAPI** (15 connections)
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **asyncio** (10 connections)
- **test_jwt_strategy.py** (10 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (9 connections) — `server/app/lifespan_startup.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_attach_combat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- *... and 96 more nodes in this community*

## Relationships

- [test_lifespan_startup.py](test_lifespan_startup.py.md) (28 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (21 shared connections)
- [get_logger](get_logger.md) (21 shared connections)
- [event_types.py](event_types.py.md) (10 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (9 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (8 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [test_users.py](test_users.py.md) (6 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (5 shared connections)
- [MythosChronicle](MythosChronicle.md) (5 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (5 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (4 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/container/__init__.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 409 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*