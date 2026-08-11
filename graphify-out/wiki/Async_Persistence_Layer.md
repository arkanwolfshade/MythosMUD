# Async Persistence Layer

> 118 nodes

## Key Concepts

- **combat.py** (50 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **test_npc_combat_data_provider.py** (14 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **Enum** (3 connections)
- **.__init__()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **.cleanup_combat_tracking()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_attacker()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_player()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_npc()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_caps_damage()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_zero_damage_when_at_zero()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **cleanup_handler()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- *... and 93 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (22 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (21 shared connections)
- [Health Check Models](Health_Check_Models.md) (18 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (14 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (12 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (10 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (10 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (8 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (7 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (7 shared connections)
- [Game Client Container](Game_Client_Container.md) (4 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 428 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*