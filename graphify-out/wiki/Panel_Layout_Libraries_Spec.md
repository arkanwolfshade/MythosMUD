# Panel Layout Libraries Spec

> 76 nodes

## Key Concepts

- **player_respawn_service.py** (41 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (40 connections) — `server/services/player_respawn_service.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **player_respawn_wrapper.py** (14 connections) — `server/game/player_respawn_wrapper.py`
- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (11 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (10 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (10 connections) — `server/services/player_respawn_service.py`
- **Player** (8 connections)
- **._clear_respawn_combat_state()** (8 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (8 connections) — `server/services/player_respawn_service.py`
- **.initialize()** (7 connections) — `server/container/bundles/combat.py`
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
- **.publish()** (5 connections) — `server/services/player_respawn_service.py`
- *... and 51 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (18 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (12 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (10 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (8 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (6 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (6 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (4 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (2 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (2 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/game/player_respawn_wrapper.py`
- `server/services/player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 343 (92%)
- INFERRED: 31 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*