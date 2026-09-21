# test_player_death_service.py

> 133 nodes

## Key Concepts

- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **PlayerDiedEvent** (31 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (31 connections) — `server/events/event_types.py`
- **asyncio** (26 connections)
- **PlayerDeathService** (25 connections) — `server/services/player_death_service.py`
- **player_death_service.py** (18 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **fixture** (7 connections)
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **mock_player()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_publishes_event()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **AsyncSession** (4 connections)
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **.handle_player_died()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_decay()** (3 connections) — `server/realtime/player_event_handlers.py`
- *... and 108 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (7 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (6 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (6 shared connections)
- [event_types.py](event_types.py.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [Stats](Stats.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [test_enhanced_logging_config.py](test_enhanced_logging_config.py.md) (3 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/services/combat_service.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 261 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*