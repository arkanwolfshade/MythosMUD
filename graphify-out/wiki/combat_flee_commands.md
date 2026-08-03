# combat flee commands

> 69 nodes

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
- **test_validate_flee_combat_and_room_success()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **.check_and_interrupt_rest()** (4 connections) — `server/commands/combat_flee.py`
- **.get_player_and_room()** (4 connections) — `server/commands/combat_flee.py`
- **UUID** (4 connections)
- **test_validate_flee_combat_and_room_no_movement_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_resolve_flee_preconditions_player_error()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Protocol** (3 connections)
- **.change_position()** (3 connections) — `server/commands/combat_flee.py`
- **.combat_service()** (3 connections) — `server/commands/combat_flee.py`
- **AppWithState** (3 connections)
- **.get_room_data()** (3 connections) — `server/commands/combat_flee.py`
- *... and 44 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (13 shared connections)
- [command factories exploration](command_factories_exploration.md) (8 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 255 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*