# Combat Taunt Tests

> 89 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (27 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
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
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
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
- *... and 64 more nodes in this community*

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (11 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (8 shared connections)
- [Player Position Service](Player_Position_Service.md) (5 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (5 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (4 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (3 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (1 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`
- `server/tests/unit/commands/test_combat_helpers.py`

## Audit Trail

- EXTRACTED: 302 (90%)
- INFERRED: 34 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*