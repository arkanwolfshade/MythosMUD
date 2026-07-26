# TauntCommandHandler

> 45 nodes · cohesion 0.05

## Key Concepts

- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (13 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target()** (9 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target_name()** (6 connections) — `server/commands/combat_taunt.py`
- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **test_run_handle_taunt_no_combat_service()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **AppWithState** (4 connections)
- **.check_and_interrupt_rest()** (4 connections) — `server/commands/combat_taunt.py`
- **.get_player_and_room()** (4 connections) — `server/commands/combat_taunt.py`
- **.resolve_combat_target()** (4 connections) — `server/commands/combat_taunt.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **test_validate_taunt_target_name_from_target_key()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.combat_service()** (3 connections) — `server/commands/combat_taunt.py`
- **.get_npc_instance()** (3 connections) — `server/commands/combat_taunt.py`
- **.validate_target_name()** (3 connections) — `server/commands/combat_taunt.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (3 connections)
- **mock_handler()** (3 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **Protocol** (1 connections)
- **Validate taunt preconditions and resolve combat/NPC.     Returns error dict or (** (1 connections) — `server/commands/combat_taunt.py`
- *... and 20 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (24 shared connections)
- [CombatInstance](CombatInstance.md) (11 shared connections)
- [TargetMatch](TargetMatch.md) (7 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 143 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*