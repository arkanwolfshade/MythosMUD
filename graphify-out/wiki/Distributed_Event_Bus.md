# Distributed Event Bus

> 39 nodes · cohesion 0.00

## Key Concepts

- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **NPCSpawnRequest** (18 connections) — `server/npc/spawning_service.py`
- **Any** (16 connections) — `server/realtime/player_event_handlers.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **Any** (11 connections) — `server/events/event_bus.py`
- **postgres_adapter.py** (11 connections) — `server/postgres_adapter.py`
- **_initialize_npc_database()** (10 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (9 connections) — `server/npc_database.py`
- **UserManager** (8 connections) — `server/game/follow_service.py`
- **Any** (8 connections) — `server/realtime/room_occupant_manager.py`
- **security_utils.py** (8 connections) — `server/security_utils.py`
- **NPCSpawnRequest** (7 connections) — `server/npc/spawning_request_execution.py`
- **UUID** (7 connections) — `server/realtime/room_occupant_manager.py`
- **Any** (6 connections) — `server/realtime/message_builders.py`
- **BoundLogger** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **UUID** (5 connections) — `server/services/player_combat_service_support.py`
- **run_test_ci.py** (4 connections) — `scripts/run_test_ci.py`
- **Task** (4 connections) — `server/events/event_bus.py`
- **Any** (4 connections) — `server/npc/lifecycle_despawn.py`
- **Any** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **T** (3 connections) — `server/events/event_bus.py`
- **async_sessionmaker** (3 connections) — `server/npc_database.py`
- **AsyncSession** (3 connections) — `server/npc_database.py`
- *... and 14 more nodes in this community*

## Relationships

- [NPC Database Sessions](NPC_Database_Sessions.md) (6 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (5 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (4 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (4 shared connections)
- [Security Infrastructure](Security_Infrastructure.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (3 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (3 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/async_persistence.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_types.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/npc_database.py`
- `server/persistence/repositories/experience_repository.py`
- `server/postgres_adapter.py`
- `server/realtime/message_builders.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/room_occupant_manager.py`
- `server/security_utils.py`
- `server/services/npc_service/queries.py`
- `server/services/player_combat_service_support.py`
- `server/structured_logging/enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 256 (81%)
- INFERRED: 59 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*