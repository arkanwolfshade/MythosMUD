# Magic Spell Service

> 129 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_startup.py** (39 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **RestartInvalidatingJWTStrategy** (15 connections) — `server/auth/jwt_strategy.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- *... and 104 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (18 shared connections)
- [Error Conversion](Error_Conversion.md) (16 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (13 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [auth users rationale](auth_users_rationale.md) (7 shared connections)
- [player death service](player_death_service.md) (4 shared connections)
- [command parser rationale](command_parser_rationale.md) (4 shared connections)
- [services npc startup](services_npc_startup.md) (4 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (3 shared connections)
- [message nats handler](message_nats_handler.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/services/npc_startup_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 552 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*