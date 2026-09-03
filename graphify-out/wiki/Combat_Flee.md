# Combat Flee

> 75 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (28 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **_FleeCommandHandlerLike** (16 connections) — `server/commands/combat_flee.py`
- **AppWithState** (15 connections) — `server/commands/combat_app_protocols.py`
- **_resolve_flee_preconditions()** (15 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (10 connections) — `server/commands/combat_helpers.py`
- **_PlayerForFlee** (8 connections) — `server/commands/combat_flee.py`
- **_ensure_flee_standing()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_room_id()** (7 connections) — `server/commands/combat_flee.py`
- **run_handle_flee_command()** (7 connections) — `server/commands/combat_flee.py`
- **combat_helpers.py** (7 connections) — `server/commands/combat_helpers.py`
- **test_validate_flee_combat_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
- **asyncio** (6 connections)
- **test_resolve_flee_preconditions_player_error()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_movement_service()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_PlayerPositionServiceLike** (4 connections) — `server/commands/combat_flee.py`
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_already_standing()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_sitting()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_combat_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **UUID** (4 connections)
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_flee.py`
- *... and 50 more nodes in this community*

## Relationships

- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (8 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (6 shared connections)
- [Combat Taunt](Combat_Taunt.md) (5 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (3 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (3 shared connections)
- [Combat Loader](Combat_Loader.md) (2 shared connections)
- [Combat Turn Processing](Combat_Turn_Processing.md) (2 shared connections)
- [Test Combat Helpers](Test_Combat_Helpers.md) (2 shared connections)
- [Combat Handler](Combat_Handler.md) (1 shared connections)
- [Combat Events](Combat_Events.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 152 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*