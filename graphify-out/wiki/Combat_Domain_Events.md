# Combat Domain Events

> 234 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat.py** (50 connections) — `server/models/combat.py`
- **CombatParticipantData** (38 connections) — `server/services/combat_types.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **combat_monitoring_service.py** (21 connections) — `server/services/combat_monitoring_service.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **chat_logger.py** (15 connections) — `server/services/chat_logger.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **test_npc_combat_data_provider.py** (14 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- **combat_service_end.py** (11 connections) — `server/services/combat_service_end.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **handle_new_login_impl()** (9 connections) — `server/realtime/connection_helpers.py`
- **apply_target_rest_and_grace_checks()** (9 connections) — `server/services/combat_service_start.py`
- **rate_limiter.py** (9 connections) — `server/services/rate_limiter.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- *... and 209 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (86 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (73 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (13 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (11 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (7 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (7 shared connections)
- [Invite Registration Model](Invite_Registration_Model.md) (6 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (6 shared connections)
- [Realtime Maintenance Connection](Realtime_Maintenance_Connection.md) (6 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (6 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (5 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (5 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/game/player_service.py`
- `server/models/combat.py`
- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/services/chat_logger.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_configuration_service.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_monitoring_service.py`
- `server/services/combat_service.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/rate_limiter.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`

## Audit Trail

- EXTRACTED: 929 (96%)
- INFERRED: 41 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*