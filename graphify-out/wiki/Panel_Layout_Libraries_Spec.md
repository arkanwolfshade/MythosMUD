# Panel Layout Libraries Spec

> 54 nodes

## Key Concepts

- **PlayerRespawnService** (40 connections) — `server/services/player_respawn_service.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (11 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (10 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (10 connections) — `server/services/player_respawn_service.py`
- **Player** (8 connections)
- **._clear_respawn_combat_state()** (8 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (8 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **.move_player_to_limbo()** (7 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (7 connections) — `server/services/player_respawn_service.py`
- **DecodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **._publish_delirium_respawn_event()** (6 connections) — `server/services/player_respawn_service.py`
- **.publish()** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **._apply_standard_respawn_state()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_standard_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_sanitarium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_delirium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **.clear_player_combat_state()** (4 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_player_state()** (4 connections) — `server/services/player_respawn_service.py`
- **._normalize_current_dp()** (3 connections) — `server/services/player_respawn_service.py`
- *... and 29 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (13 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (9 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (6 shared connections)
- [Archive Fixture Optimization](Archive_Fixture_Optimization.md) (5 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (5 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (2 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 231 (89%)
- INFERRED: 28 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*