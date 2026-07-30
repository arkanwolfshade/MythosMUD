# . init ()

> 340 nodes

## Key Concepts

- **Player** (203 connections) — `server/models/player.py`
- **player.py** (85 connections) — `server/models/player.py`
- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_respawn_service.py** (48 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **PlayerInventory** (25 connections) — `server/models/player.py`
- **PlayerRepositoryProtocol** (21 connections) — `server/persistence/protocols.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **protocols.py** (11 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **RoomRepositoryProtocol** (9 connections) — `server/persistence/protocols.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **UUID** (6 connections)
- **.get_dead_players()** (6 connections) — `server/services/player_death_service.py`
- *... and 315 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (37 shared connections)
- [real time](real_time.md) (28 shared connections)
- [Player](Player.md) (27 shared connections)
- [main()](main%28%29.md) (23 shared connections)
- [Any](Any.md) (22 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (18 shared connections)
- [UUID](UUID.md) (16 shared connections)
- [clean command input()](clean_command_input%28%29.md) (14 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (11 shared connections)
- [emote](emote.md) (11 shared connections)
- [Test get room environment() treats](Test_get_room_environment%28%29_treats.md) (10 shared connections)
- [test profession](test_profession.md) (10 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/game.py`
- `server/models/player.py`
- `server/models/player_effect.py`
- `server/persistence/protocols.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/services/test_player_death_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 1142 (89%)
- INFERRED: 138 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*