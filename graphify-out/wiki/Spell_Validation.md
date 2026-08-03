# Spell Validation

> 99 nodes

## Key Concepts

- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (46 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
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
- **.get_rewards_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
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

- [models npc rationale](models_npc_rationale.md) (19 shared connections)
- [NPC Combat](NPC_Combat.md) (15 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (10 shared connections)
- [player event realtime](player_event_realtime.md) (6 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (4 shared connections)
- [command player state](command_player_state.md) (3 shared connections)
- [room occupant manager](room_occupant_manager.md) (3 shared connections)
- [persistence rationale player](persistence_rationale_player.md) (3 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [archive 2025 AUDIT](archive_2025_AUDIT.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [persistence services combat](persistence_services_combat.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 332 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*