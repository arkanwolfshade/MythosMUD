# test exploration service

> 67 nodes

## Key Concepts

- **CombatParticipantData** (38 connections) — `server/services/combat_types.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **test_combat_initialization.py** (8 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
- **test_get_player_combat_data_uses_get_combat_stats()** (4 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_uses_get_combat_stats()** (4 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **.attacker_data()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.target_data()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_basic()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_higher_dexterity_first()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_lower_dexterity_first()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_equal_dexterity()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_auto_progression_disabled()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_different_turn_interval()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_damaged_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_zero_tick()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_combat_participant_data_creation()** (3 connections) — `server/tests/unit/services/test_combat_types.py`
- *... and 42 more nodes in this community*

## Relationships

- [Any](Any.md) (24 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (3 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (2 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 220 (94%)
- INFERRED: 15 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*