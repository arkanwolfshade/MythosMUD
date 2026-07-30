# . init ()

> 368 nodes

## Key Concepts

- **Player** (203 connections) — `server/models/player.py`
- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_respawn_service.py** (48 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **PlayerRespawnService** (39 connections) — `server/services/player_respawn_service.py`
- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **_stats_int()** (16 connections) — `server/models/player.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **int_coercion.py** (13 connections) — `server/utils/int_coercion.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **.respawn_player()** (11 connections) — `server/services/player_respawn_service.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **.respawn_player_from_delirium()** (10 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (10 connections) — `server/services/player_respawn_service.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **Player** (8 connections)
- **._clear_respawn_combat_state()** (8 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (8 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- *... and 343 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (77 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (24 shared connections)
- [Player](Player.md) (20 shared connections)
- [Any](Any.md) (19 shared connections)
- [real time](real_time.md) (19 shared connections)
- [ConnectionsComponent](ConnectionsComponent.md) (12 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (10 shared connections)
- [UUID](UUID.md) (9 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (9 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (6 shared connections)
- [Tests for get profession service](Tests_for_get_profession_service.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (5 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/models/game.py`
- `server/models/player.py`
- `server/services/player_death_service.py`
- `server/services/player_respawn_service.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/services/test_player_death_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 1191 (91%)
- INFERRED: 124 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*