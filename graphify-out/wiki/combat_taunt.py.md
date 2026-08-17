# combat_taunt.py

> 148 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **run_handle_taunt_command()** (14 connections) — `server/commands/combat_taunt.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **UUID** (11 connections)
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **_make_combat()** (8 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **on_player_entered_stealth()** (7 connections) — `server/services/aggro_threat.py`
- *... and 123 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (18 shared connections)
- [CombatParticipant](CombatParticipant.md) (17 shared connections)
- [TargetMatch](TargetMatch.md) (15 shared connections)
- [models/combat.py](models-combat.py.md) (12 shared connections)
- [CombatService](CombatService.md) (10 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (7 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [TargetType](TargetType.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 378 (94%)
- INFERRED: 24 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*