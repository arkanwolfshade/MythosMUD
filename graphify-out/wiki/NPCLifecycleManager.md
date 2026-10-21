# NPCLifecycleManager

> 225 nodes · cohesion 0.01

## Key Concepts

- **CombatService** (212 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (32 connections) — `server/services/combat_service_npc.py`
- **test_idle_movement_combat_gate.py** (31 connections) — `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **UUID** (23 connections)
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (13 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat()** (10 connections) — `server/npc/movement_integration.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **UUID** (10 connections)
- **_start_fight()** (10 connections) — `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **test_combat_service_npc_in_combat.py** (8 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **DataProviderProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_string_id_mapping()** (7 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **set_combat_service()** (7 connections) — `server/services/combat_service_state.py`
- *... and 200 more nodes in this community*

## Relationships

- [test_player_combat_service.py](test_player_combat_service.py.md) (39 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (35 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (30 shared connections)
- [DatabaseManager](DatabaseManager.md) (25 shared connections)
- [RoomService](RoomService.md) (24 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (16 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (10 shared connections)
- [ValidationError](ValidationError.md) (9 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (8 shared connections)
- [Room](Room.md) (6 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (4 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/npc/movement_integration.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 490 (81%)
- INFERRED: 117 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*