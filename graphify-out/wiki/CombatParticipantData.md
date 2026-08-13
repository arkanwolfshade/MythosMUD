# CombatParticipantData

> 64 nodes

## Key Concepts

- **CombatParticipantData** (36 connections) — `server/services/combat_types.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **test_combat_initialization.py** (8 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
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
- **.test_combat_participant_data_creation()** (3 connections) — `server/tests/unit/services/test_combat_types.py`
- **.test_combat_participant_data_current_exceeds_max()** (3 connections) — `server/tests/unit/services/test_combat_types.py`
- **.test_combat_participant_data_default_participant_type()** (3 connections) — `server/tests/unit/services/test_combat_types.py`
- *... and 39 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (27 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 123 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*