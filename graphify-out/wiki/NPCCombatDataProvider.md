# NPCCombatDataProvider

> 44 nodes

## Key Concepts

- **NPCCombatDataProvider** (43 connections) — `server/services/npc_combat_data_provider.py`
- **test_npc_combat_data_provider.py** (20 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **.get_npc_combat_data()** (9 connections) — `server/services/npc_combat_data_provider.py`
- **asyncio** (8 connections)
- **Any** (6 connections)
- **.get_player_combat_data()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **.get_npc_definition()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **._resolve_npc_behavior_snapshot()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **._resolve_npc_combat_stats()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_data_provider()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **test_get_npc_combat_data_reads_static_corruption_trait()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_definition_from_persistence()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_combat_data()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_combat_data_missing_player()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_combat_data_reads_live_corruption()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_name_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_name_unknown()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_room_id_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_room_id_invalid_uuid()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **UUID** (3 connections)
- **.get_player_name()** (2 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_room_id()** (2 connections) — `server/services/npc_combat_data_provider.py`
- **persistence()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- *... and 19 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (14 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (2 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [combat_service.py](combat_service.py.md) (1 shared connections)
- [resolve_npc_attack_damage](resolve_npc_attack_damage.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 88 (87%)
- INFERRED: 13 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*