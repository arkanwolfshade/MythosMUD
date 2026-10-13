# Community 514

> 34 nodes

## Key Concepts

- **.create_combat_instance()** (19 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (17 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **.test_add_participant_joins_and_rebuilds_initiative()** (5 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
- **.attacker_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.target_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_auto_progression_disabled()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_basic()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_damaged_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_different_turn_interval()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_threads_corruption_onto_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_equal_dexterity()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_higher_dexterity_first()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_lower_dexterity_first()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_zero_tick()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **fixture** (2 connections)
- **Test create_combat_instance orders turns by dexterity (highest first).** (2 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds *…** (1 connections) — `server/services/combat_initialization.py`
- **Create and initialize a combat instance.** (1 connections) — `server/services/combat_initialization.py`
- **Start a new combat instance between two participants.** (1 connections) — `server/services/combat_service.py`
- **Test create_combat_instance adds participants correctly.** (1 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **#815: CombatParticipantData.corruption must survive into CombatParticipant --…** (1 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **Test create_combat_instance handles equal dexterity.** (1 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 9 more nodes in this community*

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (13 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (3 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (1 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_initialization.py`

## Audit Trail

- EXTRACTED: 60 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*