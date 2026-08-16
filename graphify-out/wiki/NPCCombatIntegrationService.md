# NPCCombatIntegrationService

> 112 nodes

## Key Concepts

- **NPCCombatIntegrationService** (86 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (47 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **asyncio** (25 connections)
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **integration_service()** (7 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **_StubConfigRoot** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **test_validate_combat_location_limbo_cross_room_uses_debug()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
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
- *... and 87 more nodes in this community*

## Relationships

- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (20 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [mock_async_persistence](mock_async_persistence.md) (5 shared connections)
- [NPCBase](NPCBase.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (3 shared connections)
- [test_npc_combat_integration_service_npc_aggro.py](test_npc_combat_integration_service_npc_aggro.py.md) (3 shared connections)
- [test_npc_combat_integration_service_player_attacks.py](test_npc_combat_integration_service_player_attacks.py.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 191 (77%)
- INFERRED: 56 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*