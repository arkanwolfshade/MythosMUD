# NPCCombatIntegrationService

> 107 nodes

## Key Concepts

- **NPCCombatIntegrationService** (91 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (46 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **asyncio** (25 connections)
- **NPCCombatLifecycle** (16 connections) — `server/services/npc_combat_lifecycle.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **integration_service()** (7 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **_StubConfigRoot** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **test_validate_combat_location_limbo_cross_room_uses_debug()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **test_end_combat_if_participant_in_combat_ends_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_in_combat_no_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_skips_when_player_id_unparseable()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_get_integration_config()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_delegates_to_handle_npc_attack_on_player()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_false_when_npc_dead()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_false_without_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death_broadcast_failure_non_fatal()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death_broadcasts_room_update()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc_blocked_during_login_grace()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc_room_mismatch_ends_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 82 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (27 shared connections)
- [EventBus](EventBus.md) (10 shared connections)
- [test_npc_combat_integration_service_npc_aggro.py](test_npc_combat_integration_service_npc_aggro.py.md) (8 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_npc_combat_integration_service_player_attacks.py](test_npc_combat_integration_service_player_attacks.py.md) (3 shared connections)
- [NPCCombatRewards](NPCCombatRewards.md) (3 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (3 shared connections)
- [.handle_npc_attack_on_player](handle_npc_attack_on_player.md) (3 shared connections)
- [TestNPCCombatLifecycle](TestNPCCombatLifecycle.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 236 (90%)
- INFERRED: 26 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*