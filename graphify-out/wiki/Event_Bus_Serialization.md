# Event Bus Serialization

> 401 nodes · cohesion 0.01

## Key Concepts

- **Player** (200 connections) — `server/models/player.py`
- **player.py** (82 connections) — `server/models/player.py`
- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_respawn_service.py** (48 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (41 connections) — `server/services/player_respawn_service.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **PlayerRespawnService** (39 connections) — `server/services/player_respawn_service.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **UUID** (16 connections)
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **.respawn_player()** (11 connections) — `server/services/player_respawn_service.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **.respawn_player_from_delirium()** (10 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (10 connections) — `server/services/player_respawn_service.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **._clear_respawn_combat_state()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (8 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (8 connections) — `server/services/player_respawn_service.py`
- **Player** (8 connections)
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- *... and 376 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (52 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (26 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (18 shared connections)
- [Logging Migration Examples](Logging_Migration_Examples.md) (18 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (17 shared connections)
- [Lucidity Event Dispatcher](Lucidity_Event_Dispatcher.md) (13 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (12 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (11 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (11 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (11 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (10 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (8 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/constants/spawn_defaults.py`
- `server/container/bundles/combat.py`
- `server/models/game.py`
- `server/models/player.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/services/player_death_service.py`
- `server/services/player_respawn_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/services/test_player_death_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 1352 (91%)
- INFERRED: 135 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*