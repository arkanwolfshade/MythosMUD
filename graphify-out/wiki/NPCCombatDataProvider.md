# NPCCombatDataProvider

> 36 nodes

## Key Concepts

- **NPCCombatDataProvider** (36 connections) — `server/services/npc_combat_data_provider.py`
- **test_npc_combat_data_provider.py** (18 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **asyncio** (7 connections)
- **.get_npc_combat_data()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **.get_npc_definition()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_combat_data()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_data_provider()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **test_get_npc_definition_from_persistence()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_combat_data()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_combat_data_missing_player()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_name_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_name_unknown()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_room_id_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_room_id_invalid_uuid()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **UUID** (3 connections)
- **.get_player_name()** (2 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_room_id()** (2 connections) — `server/services/npc_combat_data_provider.py`
- **persistence()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_fallback_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_with_get_combat_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_instance_from_lifecycle()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_instance_returns_none_on_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- *... and 11 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (14 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (2 shared connections)
- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [NPCCombatLifecycle](NPCCombatLifecycle.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 65 (80%)
- INFERRED: 16 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*