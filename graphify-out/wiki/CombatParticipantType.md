# CombatParticipantType

> 77 nodes

## Key Concepts

- **CombatParticipantType** (45 connections) — `server/models/combat.py`
- **CombatParticipantData** (39 connections) — `server/services/combat_types.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **test_combat_initialization.py** (9 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **.get_npc_combat_data()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
- **.get_player_combat_data()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.attacker_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.target_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_auto_progression_disabled()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_basic()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_damaged_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_different_turn_interval()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_equal_dexterity()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 52 more nodes in this community*

## Relationships

- [test_combat_service_modules.py](test_combat_service_modules.py.md) (14 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [models/combat.py](models-combat.py.md) (8 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (7 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [CombatParticipant](CombatParticipant.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (3 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (2 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 195 (93%)
- INFERRED: 14 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*