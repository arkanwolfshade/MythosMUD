# test_player_death_service.py

> 127 nodes

## Key Concepts

- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **asyncio** (26 connections)
- **player_death_service.py** (20 connections) — `server/services/player_death_service.py`
- **PlayerDiedEvent** (16 connections) — `server/events/event_types.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **PlayerDPDecayEvent** (13 connections) — `server/events/event_types.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **fixture** (7 connections)
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **player_death_service()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **AsyncSession** (4 connections)
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 102 more nodes in this community*

## Relationships

- [RealTimeEventHandler](RealTimeEventHandler.md) (11 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [log_and_raise](log_and_raise.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [.__post_init__](__post_init__.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 238 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*