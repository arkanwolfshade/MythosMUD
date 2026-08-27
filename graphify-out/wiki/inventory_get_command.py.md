# inventory_get_command.py

> 49 nodes

## Key Concepts

- **test_combat_attack.py** (20 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **combat_attack.py** (19 connections) — `server/commands/combat_attack.py`
- **run_handle_attack_command()** (11 connections) — `server/commands/combat_attack.py`
- **asyncio** (11 connections)
- **_execute_phantom_combat_action()** (8 connections) — `server/commands/combat_attack.py`
- **Any** (8 connections)
- **_execute_combat_action()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_player_and_room()** (7 connections) — `server/commands/combat_attack.py`
- **_resolve_combat_damage()** (6 connections) — `server/commands/combat_attack.py`
- **_validate_attack_preconditions()** (6 connections) — `server/commands/combat_attack.py`
- **_get_combat_action_context()** (5 connections) — `server/commands/combat_attack.py`
- **_validate_attack_target_and_action()** (5 connections) — `server/commands/combat_attack.py`
- **test_execute_phantom_combat_action_success()** (5 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_routes_phantom_target()** (5 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_combat_action_failure_message()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_phantom_combat_action_already_dissipated()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_get_combat_action_context_missing_player()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_blocked_by_rest()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_success_path()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_incapacitated()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_missing_target()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_no_combat_zone()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_target_and_action_invalid()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **mock_handler()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_resolve_combat_damage_unarmed_fallback()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- *... and 24 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [NATSError](NATSError.md) (2 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (1 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)
- [test_npc_combat_integration_service_player_attacks.py](test_npc_combat_integration_service_player_attacks.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (1 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/tests/unit/commands/test_combat_attack.py`

## Audit Trail

- EXTRACTED: 103 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*