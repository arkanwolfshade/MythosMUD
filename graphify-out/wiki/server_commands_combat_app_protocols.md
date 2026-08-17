# server commands combat app protocols

> 68 nodes

## Key Concepts

- **TargetType** (41 connections) — `server/schemas/shared/target_resolution.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **AppWithState** (15 connections) — `server/commands/combat_app_protocols.py`
- **run_handle_taunt_command()** (14 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
- **_validate_taunt_target_name()** (5 connections) — `server/commands/combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **UUID** (5 connections)
- **_RoomWithIdOnly** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **mock_handler()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_name_from_target_key()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 43 more nodes in this community*

## Relationships

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (16 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (8 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (7 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (6 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (6 shared connections)
- [server commands combat flee](server_commands_combat_flee.md) (5 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (5 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (5 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (5 shared connections)
- [followtargetvalue](followtargetvalue.md) (3 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 186 (85%)
- INFERRED: 32 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*