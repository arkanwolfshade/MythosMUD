# PlayerRespawnEventHandler

> 228 nodes · cohesion 0.02

## Key Concepts

- **combat_service.py** (116 connections) — `server/services/combat_service.py`
- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **test_combat_service_modules.py** (65 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatParticipantData** (46 connections) — `server/services/combat_types.py`
- **asyncio** (38 connections)
- **combat_service_start.py** (34 connections) — `server/services/combat_service_start.py`
- **npc_combat_data_provider.py** (24 connections) — `server/services/npc_combat_data_provider.py`
- **npc_combat_integration_combat_mixin.py** (21 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.create_combat_instance()** (19 connections) — `server/services/combat_initialization.py`
- **combat_service_events.py** (19 connections) — `server/services/combat_service_events.py`
- **combat_types.py** (17 connections) — `server/services/combat_types.py`
- **TestCombatInitializer** (17 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (16 connections) — `server/services/combat_initialization.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **combat_hp_sync.py** (15 connections) — `server/services/combat_hp_sync.py`
- **apply_target_rest_and_grace_checks()** (14 connections) — `server/services/combat_service_start.py`
- **join_existing_combat()** (14 connections) — `server/services/combat_service_start.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (13 connections) — `server/services/combat_hp_sync.py`
- **finalize_attack_result()** (12 connections) — `server/services/combat_service_attack.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **CombatInitializer** (11 connections) — `server/services/combat_initialization.py`
- **_participant()** (11 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- *... and 203 more nodes in this community*

## Relationships

- [InventorySchemaValidationError](InventorySchemaValidationError.md) (57 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (35 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (34 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (29 shared connections)
- [Room](Room.md) (22 shared connections)
- [look_container.py](look_container.py.md) (17 shared connections)
- [stateUpdateUtils.ts](stateUpdateUtils.ts.md) (15 shared connections)
- [ValidationError](ValidationError.md) (12 shared connections)
- [DatabaseManager](DatabaseManager.md) (10 shared connections)
- [ground_channel.py](ground_channel.py.md) (10 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (10 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (9 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_types.py`
- `server/services/combat_types.py`
- `server/services/nats_exceptions.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 728 (91%)
- INFERRED: 76 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*