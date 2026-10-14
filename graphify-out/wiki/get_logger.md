# get_logger

> 1269 nodes

## Key Concepts

- **get_logger()** (559 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (534 connections) — `server/structured_logging/enhanced_logging_config.py`
- **DatabaseError** (297 connections) — `server/exceptions.py`
- **server/exceptions.py** (271 connections) — `server/exceptions.py`
- **log_and_raise()** (195 connections) — `server/utils/error_logging.py`
- **connection_manager.py** (137 connections) — `server/realtime/connection_manager.py`
- **models/player.py** (122 connections) — `server/models/player.py`
- **get_session_maker()** (111 connections) — `server/database.py`
- **time.py** (107 connections) — `server/container/bundles/time.py`
- **async_persistence.py** (105 connections) — `server/async_persistence.py`
- **server/models/__init__.py** (90 connections) — `server/models/__init__.py`
- **database.py** (89 connections) — `server/database.py`
- **get_async_session()** (68 connections) — `server/database.py`
- **Base** (65 connections) — `server/models/base.py`
- **error_logging.py** (62 connections) — `server/utils/error_logging.py`
- **models/room.py** (58 connections) — `server/models/room.py`
- **MythosMUDError** (55 connections) — `server/exceptions.py`
- **player_service.py** (55 connections) — `server/game/player_service.py`
- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **player_respawn_service.py** (51 connections) — `server/services/player_respawn_service.py`
- **bundles/game.py** (48 connections) — `server/container/bundles/game.py`
- **movement_service.py** (47 connections) — `server/game/movement_service.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **server/services/__init__.py** (43 connections) — `server/services/__init__.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- *... and 1244 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (224 shared connections)
- [EventBus](EventBus.md) (105 shared connections)
- [ContainerComponent](ContainerComponent.md) (86 shared connections)
- [CombatService](CombatService.md) (83 shared connections)
- [session](session.md) (75 shared connections)
- [alias_storage.py](alias_storage.py.md) (55 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (54 shared connections)
- [ErrorContext](ErrorContext.md) (54 shared connections)
- [Player](Player.md) (54 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (51 shared connections)
- [Room](Room.md) (45 shared connections)
- [ValidationError](ValidationError.md) (45 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `monitoring/webhook-receiver.py`
- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/api/containers.py`
- `server/api/player_helpers.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/async_persistence_types.py`
- `server/auth/argon2_utils.py`
- `server/auth/invites.py`
- `server/auth_utils.py`
- `server/commands/container_helpers_inventory_logging.py`

## Audit Trail

- EXTRACTED: 6220 (95%)
- INFERRED: 322 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*