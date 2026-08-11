# NPC Occupant Processor

> 98 nodes

## Key Concepts

- **test_command_combat.py** (30 connections) — `server/tests/unit/models/test_command_combat.py`
- **AttackCommand** (14 connections) — `server/models/command_combat.py`
- **PunchCommand** (14 connections) — `server/models/command_combat.py`
- **KickCommand** (14 connections) — `server/models/command_combat.py`
- **StrikeCommand** (14 connections) — `server/models/command_combat.py`
- **test_command_factories_combat.py** (14 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **CombatCommandFactory** (12 connections) — `server/utils/command_factories_combat.py`
- **command_factories_combat.py** (7 connections) — `server/utils/command_factories_combat.py`
- **.create_attack_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_punch_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_kick_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_strike_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_taunt_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **test_attack_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_strike_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_strike_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **.create_flee_command()** (4 connections) — `server/utils/command_factories_combat.py`
- **test_attack_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_validate_target_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- *... and 73 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (21 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (8 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Base Command Models](Base_Command_Models.md) (1 shared connections)

## Source Files

- `server/models/command_combat.py`
- `server/tests/unit/models/test_command_combat.py`
- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/utils/command_factories_combat.py`

## Audit Trail

- EXTRACTED: 293 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*