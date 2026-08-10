# Commands Look Item

> 83 nodes

## Key Concepts

- **CombatParticipantData** (38 connections) — `server/services/combat_types.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **test_npc_combat_data_provider.py** (14 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **test_combat_initialization.py** (8 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
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
- *... and 58 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (16 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (13 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (8 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (7 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (5 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (5 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (3 shared connections)
- [Health Check Models](Health_Check_Models.md) (3 shared connections)
- [Archive Planning Multiplayer](Archive_Planning_Multiplayer.md) (3 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 319 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*