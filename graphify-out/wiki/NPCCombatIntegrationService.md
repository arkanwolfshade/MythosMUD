# NPCCombatIntegrationService

> 172 nodes

## Key Concepts

- **NPCCombatIntegrationService** (86 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (47 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **asyncio** (25 connections)
- **test_npc_combat_integration_service_player_attacks.py** (23 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_npc_combat_integration_service_npc_aggro.py** (20 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **asyncio** (14 connections)
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **asyncio** (9 connections)
- **integration_service()** (7 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **_StubConfigRoot** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **mock_async_persistence()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_combat_service()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_connection_manager()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_combat_location_limbo_cross_room_uses_debug()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **fixture** (5 connections)
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc_grace_period_check_fails()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_end_combat_if_participant_in_combat_ends_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 147 more nodes in this community*

## Relationships

- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (11 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (4 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (4 shared connections)
- [NPCCombatLifecycle](NPCCombatLifecycle.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [CombatMessagingIntegration](CombatMessagingIntegration.md) (2 shared connections)
- [NPCCombatRewards](NPCCombatRewards.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 273 (81%)
- INFERRED: 64 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*