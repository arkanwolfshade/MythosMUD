# Panel Layout Libraries Spec

> 76 nodes

## Key Concepts

- **PlayerRespawnService** (40 connections) — `server/services/player_respawn_service.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **player_respawn_wrapper.py** (14 connections) — `server/game/player_respawn_wrapper.py`
- **.respawn_player()** (11 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (10 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (10 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnWrapper** (8 connections) — `server/game/player_respawn_wrapper.py`
- **Player** (8 connections)
- **._clear_respawn_combat_state()** (8 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **AsyncSession** (7 connections)
- **.move_player_to_limbo()** (7 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (7 connections) — `server/services/player_respawn_service.py`
- **DecodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **EncodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **.respawn_player_by_user_id()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **_RespawnEventPublisher** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (6 connections) — `server/services/player_respawn_service.py`
- **._publish_delirium_respawn_event()** (6 connections) — `server/services/player_respawn_service.py`
- **.publish()** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **._apply_standard_respawn_state()** (5 connections) — `server/services/player_respawn_service.py`
- *... and 51 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (20 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (14 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (10 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (7 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (6 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (2 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 295 (89%)
- INFERRED: 35 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*