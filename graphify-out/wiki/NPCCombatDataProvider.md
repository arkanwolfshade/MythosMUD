# NPCCombatDataProvider

> 31 nodes

## Key Concepts

- **NPCCombatDataProvider** (36 connections) — `server/services/npc_combat_data_provider.py`
- **test_npc_combat_data_provider.py** (18 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **asyncio** (7 connections)
- **.get_npc_definition()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
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
- **.get_player_name()** (2 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_room_id()** (2 connections) — `server/services/npc_combat_data_provider.py`
- **persistence()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_fallback_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_with_get_combat_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_instance_from_lifecycle()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_instance_returns_none_on_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **fixture** (1 connections)
- **Get player name for messaging. Args: player_id: ID of the player Returns:…** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get the current room ID for a player. Args: player_id: ID of the player (must…** (1 connections) — `server/services/npc_combat_data_provider.py`
- *... and 6 more nodes in this community*

## Relationships

- [models/combat.py](models-combat.py.md) (8 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (7 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [.connection_manager](connection_manager.md) (2 shared connections)
- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 58 (78%)
- INFERRED: 16 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*