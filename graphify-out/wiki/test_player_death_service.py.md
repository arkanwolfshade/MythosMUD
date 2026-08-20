# test_player_death_service.py

> 123 nodes

## Key Concepts

- **test_player_death_service.py** (53 connections) — `server/tests/unit/services/test_player_death_service.py`
- **asyncio** (26 connections)
- **PlayerDeathService** (25 connections) — `server/services/player_death_service.py`
- **player_death_service.py** (20 connections) — `server/services/player_death_service.py`
- **PositionState** (17 connections) — `server/models/game.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **fixture** (7 connections)
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **PlayerLifecycleServices** (5 connections) — `server/services/combat_service_types.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **mock_player()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_publishes_event()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **AsyncSession** (4 connections)
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 98 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (13 shared connections)
- [NATSError](NATSError.md) (10 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [server/models/game.py](server-models-game.py.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [test_enhanced_logging_config.py](test_enhanced_logging_config.py.md) (3 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)

## Source Files

- `server/models/game.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 229 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*