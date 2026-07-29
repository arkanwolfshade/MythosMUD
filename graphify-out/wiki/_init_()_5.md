# . init ()

> 442 nodes

## Key Concepts

- **Player** (199 connections) — `server/models/player.py`
- **player.py** (83 connections) — `server/models/player.py`
- **PlayerLucidity** (73 connections) — `server/models/lucidity.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_respawn_service.py** (48 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (41 connections) — `server/services/player_respawn_service.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **PlayerRespawnService** (39 connections) — `server/services/player_respawn_service.py`
- **lucidity.py** (33 connections) — `server/models/lucidity.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **game.py** (32 connections) — `server/models/game.py`
- **service.py** (30 connections) — `server/services/passive_lucidity_flux/service.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **PlayerInventory** (25 connections) — `server/models/player.py`
- **PlayerRepositoryProtocol** (21 connections) — `server/persistence/protocols.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **PlayerSkill** (17 connections) — `server/models/player_skill.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **player_respawn_wrapper.py** (14 connections) — `server/game/player_respawn_wrapper.py`
- *... and 417 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (95 shared connections)
- [. init ()](_init_%28%29.md) (41 shared connections)
- [Any](Any.md) (31 shared connections)
- [Base](Base.md) (29 shared connections)
- [datetime](datetime.md) (23 shared connections)
- [Connection Manager](Connection_Manager.md) (22 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (20 shared connections)
- [config](config.md) (19 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (17 shared connections)
- [PlayerChannelPreferences](PlayerChannelPreferences.md) (16 shared connections)
- [APIRouter](APIRouter.md) (16 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (13 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/combat.py`
- `server/game/player_respawn_wrapper.py`
- `server/models/game.py`
- `server/models/lucidity.py`
- `server/models/player.py`
- `server/models/player_effect.py`
- `server/models/player_skill.py`
- `server/persistence/protocols.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_room.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/services/combat_service_types.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/services/player_death_service.py`
- `server/services/player_respawn_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 1765 (89%)
- INFERRED: 220 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*