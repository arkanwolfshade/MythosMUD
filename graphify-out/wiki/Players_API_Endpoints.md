# Players API Endpoints

> 93 nodes

## Key Concepts

- **CombatParticipantData** (38 connections) — `server/services/combat_types.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **apply_target_rest_and_grace_checks()** (9 connections) — `server/services/combat_service_start.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **check_attacker_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **test_combat_initialization.py** (8 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **get_connection_manager_for_combat_check()** (7 connections) — `server/services/combat_service_start.py`
- **check_target_rest_and_grace_period()** (7 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (7 connections) — `server/services/combat_service_start.py`
- **register_combat()** (6 connections) — `server/services/combat_service_start.py`
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
- **.check_connection_state()** (5 connections) — `server/services/combat_cleanup_handler.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **validate_combat_can_start()** (5 connections) — `server/services/combat_service_start.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
- **test_get_player_combat_data_uses_get_combat_stats()** (4 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_uses_get_combat_stats()** (4 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- *... and 68 more nodes in this community*

## Relationships

- [Async Persistence Layer](Async_Persistence_Layer.md) (14 shared connections)
- [Health Check Models](Health_Check_Models.md) (12 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (11 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (7 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (5 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (5 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Command Parser](Command_Parser.md) (3 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (2 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_start.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 332 (91%)
- INFERRED: 31 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*