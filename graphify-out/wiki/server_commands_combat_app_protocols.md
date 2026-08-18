# server commands combat app protocols

> 158 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **TargetType** (41 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (38 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **AppWithState** (15 connections) — `server/commands/combat_app_protocols.py`
- **run_handle_taunt_command()** (14 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **asyncio** (12 connections)
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_as_app_with_state()** (9 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_get_player_and_room_no_current_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **test_resolve_combat_target_rejects_dead_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_non_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 133 more nodes in this community*

## Relationships

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (19 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (16 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server commands combat](server_commands_combat.md) (8 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (7 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (6 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (6 shared connections)
- [server events combat events](server_events_combat_events.md) (6 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (6 shared connections)
- [server models combat](server_models_combat.md) (6 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (6 shared connections)
- [server commands combat flee](server_commands_combat_flee.md) (5 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 359 (87%)
- INFERRED: 53 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*