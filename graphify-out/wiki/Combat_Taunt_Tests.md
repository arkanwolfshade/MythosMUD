# Combat Taunt Tests

> 84 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (27 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **_FleeCommandHandlerLike** (17 connections) — `server/commands/combat_flee.py`
- **_resolve_flee_preconditions()** (15 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (12 connections) — `server/commands/combat_helpers.py`
- **_PlayerForFlee** (11 connections) — `server/commands/combat_flee.py`
- **_ensure_flee_standing()** (11 connections) — `server/commands/combat_flee.py`
- **_PlayerPositionServiceLike** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_room_id()** (8 connections) — `server/commands/combat_flee.py`
- **combat_helpers.py** (7 connections) — `server/commands/combat_helpers.py`
- **run_handle_flee_command()** (6 connections) — `server/commands/combat_flee.py`
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **test_combat_helpers.py** (6 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_validate_flee_combat_and_room_success()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **.check_and_interrupt_rest()** (4 connections) — `server/commands/combat_flee.py`
- **.get_player_and_room()** (4 connections) — `server/commands/combat_flee.py`
- **UUID** (4 connections)
- **test_validate_flee_combat_and_room_no_movement_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_resolve_flee_preconditions_player_error()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Protocol** (3 connections)
- **.change_position()** (3 connections) — `server/commands/combat_flee.py`
- *... and 59 more nodes in this community*

## Relationships

- [Combat Death Handling](Combat_Death_Handling.md) (8 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (5 shared connections)
- [Container Open Events](Container_Open_Events.md) (5 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (3 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (2 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (2 shared connections)
- [Health Check Models](Health_Check_Models.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`
- `server/tests/unit/commands/test_combat_helpers.py`

## Audit Trail

- EXTRACTED: 286 (92%)
- INFERRED: 24 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*