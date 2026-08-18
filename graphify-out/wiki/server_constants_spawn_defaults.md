# server constants spawn defaults

> 157 nodes

## Key Concepts

- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (36 connections) — `server/services/player_respawn_service.py`
- **asyncio** (27 connections)
- **PositionState** (17 connections) — `server/models/game.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (13 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_liability_update()** (11 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **spawn_defaults.py** (8 connections) — `server/constants/spawn_defaults.py`
- **Player** (8 connections)
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (7 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **fixture** (7 connections)
- **DecodeLiabilitiesFn** (6 connections) — `server/utils/liability_types.py`
- **EncodeLiabilitiesFn** (6 connections) — `server/utils/liability_types.py`
- **._clear_respawn_combat_state()** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (5 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (5 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (5 connections) — `server/services/player_respawn_service.py`
- **._apply_standard_respawn_state()** (5 connections) — `server/services/player_respawn_service.py`
- *... and 132 more nodes in this community*

## Relationships

- [server models lucidity](server_models_lucidity.md) (24 shared connections)
- [server async persistence](server_async_persistence.md) (18 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (10 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (9 shared connections)
- [server api character creation](server_api_character_creation.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server services combat service types](server_services_combat_service_types.md) (4 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (4 shared connections)
- [server models player player apply](server_models_player_player_apply.md) (4 shared connections)
- [server api player respawn](server_api_player_respawn.md) (2 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/models/game.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 326 (91%)
- INFERRED: 34 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*