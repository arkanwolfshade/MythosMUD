# Application Config Settings

> 69 nodes

## Key Concepts

- **test_player_respawn_service.py** (48 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **test_respawn_player_from_delirium_success()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service_no_deps()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_player()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_dead_player()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_utc_now()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_success()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_refused_when_not_dead()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_custom()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_default()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_combat_clear_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_clears_combat_state()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_no_combat_service()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **datetime** (2 connections)
- **mock_event_bus()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_player_combat_service()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 44 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (12 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (8 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (6 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (2 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 164 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*