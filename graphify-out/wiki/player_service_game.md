# player service game

> 119 nodes

## Key Concepts

- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **.get_mortally_wounded_players()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **player_death_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_publishes_event()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_with_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 94 more nodes in this community*

## Relationships

- [inventory mutation guard](inventory_mutation_guard.md) (12 shared connections)
- [game weapon player](game_weapon_player.md) (8 shared connections)
- [aggro threat services](aggro_threat_services.md) (6 shared connections)
- [nats services service](nats_services_service.md) (5 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (4 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (3 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (3 shared connections)
- [room renderer functions](room_renderer_functions.md) (2 shared connections)

## Source Files

- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 324 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*