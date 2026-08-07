# grace period login

> 99 nodes

## Key Concepts

- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (46 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **_StubConfigRoot** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **integration_service()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **test_integration_service_init_with_shared_player_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_integration_service_init_creates_combat_service_when_none()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_combat_location_limbo_cross_room_uses_debug()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_player_combat_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_messaging_integration()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_combat_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_data_provider()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_lucidity_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **_StubGameConfig** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_integration_service_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_get_integration_config()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_is_auto_progression_enabled()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_and_get_npc_instance_provided()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_and_get_npc_instance_lookup()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_and_get_npc_instance_dead()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_combat_location()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 74 more nodes in this community*

## Relationships

- [models player rationale](models_player_rationale.md) (8 shared connections)
- [player event realtime](player_event_realtime.md) (8 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [auth users rationale](auth_users_rationale.md) (6 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (5 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (4 shared connections)
- [connection models realtime](connection_models_realtime.md) (4 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [room sync service](room_sync_service.md) (3 shared connections)
- [commands position system](commands_position_system.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 329 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*