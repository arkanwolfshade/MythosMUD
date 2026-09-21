# CombatInstance

> 203 nodes

## Key Concepts

- **CombatInstance** (201 connections) — `server/models/combat.py`
- **combat_taunt.py** (34 connections) — `server/commands/combat_taunt.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **aggro_threat.py** (30 connections) — `server/services/aggro_threat.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **add_heal_threat()** (15 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **_apply_taunt_and_maybe_broadcast()** (11 connections) — `server/commands/combat_taunt.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **UUID** (11 connections)
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **UUID** (10 connections)
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- *... and 178 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (65 shared connections)
- [get_logger](get_logger.md) (46 shared connections)
- [CombatService](CombatService.md) (44 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (36 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (25 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (20 shared connections)
- [TargetMatch](TargetMatch.md) (14 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (13 shared connections)
- [spell_effects.py](spell_effects.py.md) (13 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (11 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (8 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (7 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 674 (94%)
- INFERRED: 41 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*