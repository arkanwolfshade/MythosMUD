# test rate limiter utils

> 109 nodes

## Key Concepts

- **PlayerLucidity** (73 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityExposureState** (23 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **LucidityRepository** (14 connections) — `server/services/lucidity_repository.py`
- **lucidity_repository.py** (11 connections) — `server/services/lucidity_repository.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **UUID** (9 connections)
- **test_lucidity_adjustment_round_trip()** (7 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **.delete_cooldowns_by_action_code_pattern()** (6 connections) — `server/services/lucidity_repository.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **_utc_now()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **Base** (4 connections)
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/services/lucidity_service.py`
- *... and 84 more nodes in this community*

## Relationships

- [UUID](UUID.md) (30 shared connections)
- [. init ()](_init_%28%29.md) (18 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (13 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (7 shared connections)
- [main()](main%28%29.md) (7 shared connections)
- [config](config.md) (7 shared connections)
- [map helpers](map_helpers.md) (6 shared connections)
- [CommandExecutionRequest](CommandExecutionRequest.md) (4 shared connections)
- [test command factories communication](test_command_factories_communication.md) (4 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)
- [test player preferences service](test_player_preferences_service.md) (3 shared connections)
- [Test get room environment() treats](Test_get_room_environment%28%29_treats.md) (3 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/tests/unit/services/test_rescue_service.py`

## Audit Trail

- EXTRACTED: 376 (89%)
- INFERRED: 48 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*