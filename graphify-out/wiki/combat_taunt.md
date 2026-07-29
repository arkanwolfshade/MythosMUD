# combat taunt

> 151 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TargetType** (30 connections) — `server/schemas/shared/target_resolution.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **_validate_taunt_context()** (13 connections) — `server/commands/combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **UUID** (11 connections)
- **_validate_taunt_target()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_combat()** (8 connections) — `server/tests/integration/test_aggro_flow.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- *... and 126 more nodes in this community*

## Relationships

- [combat](combat.md) (58 shared connections)
- [Spell Targeting](Spell_Targeting.md) (24 shared connections)
- [Player Position Service](Player_Position_Service.md) (16 shared connections)
- [Any](Any.md) (8 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (7 shared connections)
- [.end combat()](end_combat%28%29.md) (3 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (3 shared connections)
- [get current tick()](get_current_tick%28%29.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [init](init.md) (2 shared connections)
- [follow commands](follow_commands.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/aggro_threat.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 731 (98%)
- INFERRED: 14 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*