# player room realtime

> 388 nodes

## Key Concepts

- **player.py** (93 connections) — `server/models/player.py`
- **LucidityService** (88 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (78 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **player_respawn_service.py** (44 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (39 connections) — `server/services/player_respawn_service.py`
- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **lucidity.py** (34 connections) — `server/models/lucidity.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerChannelPreferences** (30 connections) — `server/models/player.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **LucidityExposureState** (26 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (25 connections) — `server/models/lucidity.py`
- **PlayerInventory** (25 connections) — `server/models/player.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_service.py** (24 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **LucidityAdjustmentLog** (23 connections) — `server/models/lucidity.py`
- **test_lucidity_repository.py** (22 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **_stats_int()** (16 connections) — `server/models/player.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **UUID** (14 connections)
- *... and 363 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (61 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (54 shared connections)
- [command factories create](command_factories_create.md) (24 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (18 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (18 shared connections)
- [Spell Validation](Spell_Validation.md) (18 shared connections)
- [Error Conversion](Error_Conversion.md) (14 shared connections)
- [NATS Messaging](NATS_Messaging.md) (13 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (12 shared connections)
- [player service game](player_service_game.md) (11 shared connections)
- [profession models rationale](profession_models_rationale.md) (10 shared connections)
- [add used user](add_used_user.md) (9 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/models/lucidity.py`
- `server/models/player.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/player_preferences_service.py`
- `server/services/player_respawn_service.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/models/test_player_related_models.py`
- `server/tests/unit/services/test_lucidity_repository.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_player_preferences_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 1692 (90%)
- INFERRED: 184 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*