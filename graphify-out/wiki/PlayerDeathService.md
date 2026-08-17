# PlayerDeathService

> 27 nodes

## Key Concepts

- **PlayerDeathService** (25 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **Exception** (1 connections)
- **Process DP decay for a single mortally wounded player. Decreases player DP by…** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead. Args: player: Player object to…** (1 connections) — `server/services/player_death_service.py`
- **Clear player combat state when they die. BUGFIX #244: As documented in…** (1 connections) — `server/services/player_death_service.py`
- **Get room name for death location display. Args: death_location: Room ID where…** (1 connections) — `server/services/player_death_service.py`
- **Publish player died event if event bus is available. Args: player_id: ID of the…** (1 connections) — `server/services/player_death_service.py`
- **Service for managing player death, mortally wounded state, and DP decay. This…** (1 connections) — `server/services/player_death_service.py`
- **Handle player death when DP reaches -10 or below. Records death location and…** (1 connections) — `server/services/player_death_service.py`
- **Initialize the player death service. Args: event_bus: Optional event bus for…** (1 connections) — `server/services/player_death_service.py`
- **Get all players currently in the mortally wounded state. A player is considered…** (1 connections) — `server/services/player_death_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [combat_service_types.py](combat_service_types.py.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 65 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*