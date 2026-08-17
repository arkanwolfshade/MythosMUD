# server commands combat flee

> 70 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (28 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **_FleeCommandHandlerLike** (16 connections) — `server/commands/combat_flee.py`
- **_resolve_flee_preconditions()** (15 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (10 connections) — `server/commands/combat_helpers.py`
- **_PlayerForFlee** (8 connections) — `server/commands/combat_flee.py`
- **_ensure_flee_standing()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **run_handle_flee_command()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_room_id()** (7 connections) — `server/commands/combat_flee.py`
- **combat_helpers.py** (7 connections) — `server/commands/combat_helpers.py`
- **test_validate_flee_combat_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
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
- **.combat_service()** (3 connections) — `server/commands/combat_flee.py`
- **.get_player_and_room()** (3 connections) — `server/commands/combat_flee.py`
- *... and 45 more nodes in this community*

## Relationships

- [server models combat combatinstance](server_models_combat_combatinstance.md) (8 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (5 shared connections)
- [server commands combat](server_commands_combat.md) (4 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (4 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (3 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 141 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*