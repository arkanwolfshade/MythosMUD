# NPCCombatDataProvider

> 68 nodes

## Key Concepts

- **NPCCombatDataProvider** (41 connections) — `server/services/npc_combat_data_provider.py`
- **npc_combat_data_provider.py** (20 connections) — `server/services/npc_combat_data_provider.py`
- **test_npc_combat_data_provider.py** (20 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **asyncio** (8 connections)
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_npc_combat_data()** (6 connections) — `server/services/npc_combat_data_provider.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_player_combat_data()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **combat_messaging_integration.py** (5 connections) — `server/services/combat_messaging_integration.py`
- **UUID** (5 connections)
- **.get_npc_definition()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **._broadcast_npc_attack_on_player_started()** (3 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_data_provider()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **test_get_npc_combat_data_reads_static_corruption_trait()** (3 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- *... and 43 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (19 shared connections)
- [combat_service.py](combat_service.py.md) (13 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [event_types.py](event_types.py.md) (5 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (4 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [combat_attack.py](combat_attack.py.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [.connection_manager](connection_manager.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging_integration.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 160 (91%)
- INFERRED: 15 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*