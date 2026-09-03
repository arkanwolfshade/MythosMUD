# Test Movement Service

> 99 nodes

## Key Concepts

- **test_movement_service.py** (52 connections) — `server/tests/unit/game/test_movement_service.py`
- **movement_service.py** (36 connections) — `server/game/movement_service.py`
- **player_combat_service.py** (23 connections) — `server/services/player_combat_service.py`
- **asyncio** (20 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **test_move_player_empty_player_id()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_from_room()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_to_room()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_auto_add()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_db_mismatch()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_room_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_success()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_allows_without_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_blocks_when_in_combat()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_player_posture_blocks_sitting()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 74 more nodes in this community*

## Relationships

- [Movement Service](Movement_Service.md) (10 shared connections)
- [Test Player Combat Service](Test_Player_Combat_Service.md) (6 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (6 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Async Persistence](Async_Persistence.md) (4 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (4 shared connections)
- [Test Movement Service](Test_Movement_Service.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (2 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 220 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*