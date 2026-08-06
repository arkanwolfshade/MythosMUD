# player room realtime

> 451 nodes

## Key Concepts

- **player.py** (93 connections) — `server/models/player.py`
- **PlayerLucidity** (78 connections) — `server/models/lucidity.py`
- **__init__.py** (73 connections) — `server/models/__init__.py`
- **Base** (60 connections) — `server/models/base.py`
- **test_player_respawn_service.py** (54 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (44 connections) — `server/services/player_respawn_service.py`
- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **lucidity.py** (34 connections) — `server/models/lucidity.py`
- **service.py** (30 connections) — `server/services/passive_lucidity_flux/service.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **test_world.py** (27 connections) — `server/tests/unit/models/test_world.py`
- **LucidityExposureState** (26 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (25 connections) — `server/models/lucidity.py`
- **PlayerInventory** (25 connections) — `server/models/player.py`
- **LucidityAdjustmentLog** (23 connections) — `server/models/lucidity.py`
- **PlayerSpell** (23 connections) — `server/models/player_spells.py`
- **base.py** (22 connections) — `server/models/base.py`
- **test_lucidity_repository.py** (22 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_item.py** (19 connections) — `server/tests/unit/models/test_item.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **_stats_int()** (16 connections) — `server/models/player.py`
- **player_respawn_wrapper.py** (15 connections) — `server/game/player_respawn_wrapper.py`
- *... and 426 more nodes in this community*

## Relationships

- [game weapon player](game_weapon_player.md) (45 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (45 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (23 shared connections)
- [room renderer functions](room_renderer_functions.md) (16 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (16 shared connections)
- [event events serialization](event_events_serialization.md) (15 shared connections)
- [command factories create](command_factories_create.md) (14 shared connections)
- [player requests schemas](player_requests_schemas.md) (13 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (12 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (11 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (10 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/game/player_respawn_wrapper.py`
- `server/metadata.py`
- `server/models/__init__.py`
- `server/models/base.py`
- `server/models/calendar.py`
- `server/models/dialogue.py`
- `server/models/emote.py`
- `server/models/item.py`
- `server/models/lucidity.py`
- `server/models/player.py`
- `server/models/player_effect.py`
- `server/models/player_spells.py`
- `server/models/skill_use_log.py`
- `server/models/spell_db.py`
- `server/models/world.py`
- `server/npc_metadata.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/services/lucidity_repository.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 1742 (91%)
- INFERRED: 169 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*