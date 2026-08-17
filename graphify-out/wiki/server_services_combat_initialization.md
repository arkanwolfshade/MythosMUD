# server services combat initialization

> 69 nodes

## Key Concepts

- **CombatParticipantData** (35 connections) — `server/services/combat_types.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
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
- **.test_create_combat_instance_turn_order_higher_dexterity_first()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_turn_order_lower_dexterity_first()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_zero_tick()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 44 more nodes in this community*

## Relationships

- [server app game tick counter](server_app_game_tick_counter.md) (20 shared connections)
- [server services npc combat data](server_services_npc_combat_data.md) (4 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (4 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (3 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 128 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*