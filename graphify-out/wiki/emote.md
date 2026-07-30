# emote

> 82 nodes

## Key Concepts

- **PlayerRespawnService** (39 connections) — `server/services/player_respawn_service.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **.respawn_player()** (11 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (10 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (10 connections) — `server/services/player_respawn_service.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **Player** (8 connections)
- **._clear_respawn_combat_state()** (8 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (8 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **.move_player_to_limbo()** (7 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (7 connections) — `server/services/player_respawn_service.py`
- **DecodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **EncodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **_RespawnEventPublisher** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (6 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (6 connections) — `server/services/player_respawn_service.py`
- **._publish_delirium_respawn_event()** (6 connections) — `server/services/player_respawn_service.py`
- **.clear_liability()** (5 connections) — `server/services/lucidity_service.py`
- **.publish()** (5 connections) — `server/services/player_respawn_service.py`
- *... and 57 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (13 shared connections)
- [UUID](UUID.md) (11 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (11 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (8 shared connections)
- [real time](real_time.md) (6 shared connections)
- [clean command input()](clean_command_input%28%29.md) (3 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 313 (90%)
- INFERRED: 35 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*