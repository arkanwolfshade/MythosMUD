# PlayerDeathService

> 33 nodes

## Key Concepts

- **PlayerDeathService** (25 connections) — `server/services/player_death_service.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **._get_room_name_for_death()** (3 connections) — `server/services/player_death_service.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **Exception** (1 connections)
- **Initialize combat services.** (1 connections) — `server/container/bundles/combat.py`
- **Small types shared by CombatService wiring.** (1 connections) — `server/services/combat_service_types.py`
- **Player Death Service for managing player mortality and DP decay. This service…** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player. Decreases player DP by…** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead. Args: player: Player object to…** (1 connections) — `server/services/player_death_service.py`
- **Clear player combat state when they die. BUGFIX #244: As documented in…** (1 connections) — `server/services/player_death_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [PlayerEnteredRoom](PlayerEnteredRoom.md) (6 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (5 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (4 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (2 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 91 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*