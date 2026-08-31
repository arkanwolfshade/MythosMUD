# .create_combat_instance

> 34 nodes

## Key Concepts

- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **.attacker_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.target_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_auto_progression_disabled()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_basic()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_damaged_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_different_turn_interval()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_equal_dexterity()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_higher_dexterity_first()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_lower_dexterity_first()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_zero_tick()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **UUID** (2 connections)
- **fixture** (2 connections)
- **Build CombatParticipant from CombatParticipantData.** (1 connections) — `server/services/combat_initialization.py`
- **Return participant IDs sorted by dexterity (highest first).** (1 connections) — `server/services/combat_initialization.py`
- **Create and initialize a combat instance.** (1 connections) — `server/services/combat_initialization.py`
- **Start a new combat instance between two participants.** (1 connections) — `server/services/combat_service.py`
- **Test create_combat_instance orders turns when target has higher dexterity.** (1 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **Test create_combat_instance handles equal dexterity.** (1 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **Test create_combat_instance with auto-progression disabled.** (1 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 9 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (7 shared connections)
- [NATSError](NATSError.md) (7 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_initialization.py`

## Audit Trail

- EXTRACTED: 56 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*