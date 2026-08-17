# NPCCombatDataProvider

> 34 nodes

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
- **fixture** (1 connections)
- *... and 9 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (10 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (3 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (2 shared connections)
- [combat_service_attack.py](combat_service_attack.py.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [NPCCombatLifecycle](NPCCombatLifecycle.md) (1 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)
- [._handle_npc_death_on_combat_end](_handle_npc_death_on_combat_end.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 63 (80%)
- INFERRED: 16 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*