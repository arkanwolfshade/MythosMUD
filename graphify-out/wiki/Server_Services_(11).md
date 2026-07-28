# Server Services (11)

> 121 nodes

## Key Concepts

- **NPCCombatIntegrationService** (89 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (44 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **_StubConfigRoot** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **integration_service()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **test_integration_service_init_with_shared_player_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_integration_service_init_creates_combat_service_when_none()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_player_combat_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_combat_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_data_provider()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **._complete_player_attack_on_npc_after_grace()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (3 connections)
- *... and 96 more nodes in this community*

## Relationships

- [Server Services (4)](Server_Services_%284%29.md) (15 shared connections)
- [Server Services (27)](Server_Services_%2827%29.md) (9 shared connections)
- [Server Services (32)](Server_Services_%2832%29.md) (9 shared connections)
- [Server Npc](Server_Npc.md) (7 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (4 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (4 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (4 shared connections)
- [Server Services (73)](Server_Services_%2873%29.md) (4 shared connections)
- [Server Events](Server_Events.md) (3 shared connections)
- [Server Services (44)](Server_Services_%2844%29.md) (3 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (3 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 388 (93%)
- INFERRED: 30 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*