# .create_combat_instance

> 36 nodes

## Key Concepts

- **.create_combat_instance()** (18 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (16 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
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
- **UUID** (2 connections)
- **fixture** (2 connections)
- **Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds *…** (1 connections) — `server/services/combat_initialization.py`
- **Build CombatParticipant from CombatParticipantData.** (1 connections) — `server/services/combat_initialization.py`
- **Return participant IDs sorted by dexterity (highest first).** (1 connections) — `server/services/combat_initialization.py`
- **Create and initialize a combat instance.** (1 connections) — `server/services/combat_initialization.py`
- **#815: CombatParticipantData.corruption must survive into CombatParticipant --…** (1 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **Test create_combat_instance orders turns by dexterity (highest first).** (1 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 11 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (14 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/tests/unit/services/test_combat_initialization.py`

## Audit Trail

- EXTRACTED: 58 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*