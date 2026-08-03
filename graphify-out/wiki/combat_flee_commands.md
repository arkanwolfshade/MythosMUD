# combat flee commands

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

- [NPC Combat](NPC_Combat.md) (17 shared connections)
- [Item Instances](Item_Instances.md) (11 shared connections)
- [target resolution service](target_resolution_service.md) (5 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (3 shared connections)
- [command factories exploration](command_factories_exploration.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)

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