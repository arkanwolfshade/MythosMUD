# combat models rationale

> 214 nodes

## Key Concepts

- **PlayerLucidity** (78 connections) — `server/models/lucidity.py`
- **test_player_respawn_service.py** (54 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **player_respawn_service.py** (44 connections) — `server/services/player_respawn_service.py`
- **game.py** (32 connections) — `server/models/game.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **player_respawn_wrapper.py** (15 connections) — `server/game/player_respawn_wrapper.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **.respawn_player_from_delirium_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **test_lucidity_service_smoke.py** (6 connections) — `server/tests/unit/test_lucidity_service_smoke.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **._get_player_from_record_inspect()** (4 connections) — `server/services/lucidity_service.py`
- **test_respawn_player_from_delirium_success()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_sanitarium_success()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_lucidity_service_apply_adjustment()** (4 connections) — `server/tests/unit/test_lucidity_service_smoke.py`
- **StrEnum** (3 connections)
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **Any** (3 connections)
- *... and 189 more nodes in this community*

## Relationships

- [world models rationale](world_models_rationale.md) (91 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (16 shared connections)
- [command helpers functions](command_helpers_functions.md) (11 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (9 shared connections)
- [combat services persistence](combat_services_persistence.md) (9 shared connections)
- [Database Config](Database_Config.md) (8 shared connections)
- [command inventory models](command_inventory_models.md) (7 shared connections)
- [player service game](player_service_game.md) (7 shared connections)
- [command inventory factories](command_inventory_factories.md) (6 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (6 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/models/game.py`
- `server/models/lucidity.py`
- `server/services/lucidity_service.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 660 (92%)
- INFERRED: 55 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*