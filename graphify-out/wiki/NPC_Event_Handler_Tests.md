# NPC Event Handler Tests

> 68 nodes

## Key Concepts

- **PlayerPositionService** (45 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **.change_position()** (10 connections) — `server/services/player_position_service.py`
- **Any** (7 connections)
- **._get_player_for_position_change()** (5 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (5 connections) — `server/services/player_position_service.py`
- **._extract_player_info()** (4 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (4 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (4 connections) — `server/services/player_position_service.py`
- **test_change_position_database_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **.__init__()** (3 connections) — `server/services/player_position_service.py`
- **.ensure_default_aliases()** (3 connections) — `server/services/player_position_service.py`
- **._validate_position()** (3 connections) — `server/services/player_position_service.py`
- **test_player_position_service_init()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_player_position_service_init_none_values()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_no_storage()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_creates_missing()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_updates_incorrect()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_keeps_correct()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_handles_errors()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_invalid_position()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_persistence()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_already_in_position()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (2 shared connections)
- [Player State Factories](Player_State_Factories.md) (2 shared connections)
- [Player Respawn Handlers](Player_Respawn_Handlers.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 220 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*