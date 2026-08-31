# test_player_death_service.py

> 122 nodes

## Key Concepts

- **test_player_death_service.py** (53 connections) — `server/tests/unit/services/test_player_death_service.py`
- **PlayerDPDecayEvent** (29 connections) — `server/events/event_types.py`
- **asyncio** (26 connections)
- **PlayerDeathService** (25 connections) — `server/services/player_death_service.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
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
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **.handle_player_dp_decay()** (3 connections) — `server/realtime/player_event_handlers.py`
- **._get_room_name_for_death()** (3 connections) — `server/services/player_death_service.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 97 more nodes in this community*

## Relationships

- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (10 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (5 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (2 shared connections)
- [game_tick_protocols.py](game_tick_protocols.py.md) (2 shared connections)
- [emit_posture_change](emit_posture_change.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 227 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*