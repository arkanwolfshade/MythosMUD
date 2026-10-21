# _MigrationArgs

> 32 nodes · cohesion 0.10

## Key Concepts

- **player_combat_service.py** (26 connections) — `server/services/player_combat_service.py`
- **player_combat_service_support.py** (17 connections) — `server/services/player_combat_service_support.py`
- **LevelServiceLike** (6 connections) — `server/services/player_combat_service_support.py`
- **NPCCombatIntegrationReadApi** (6 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **UUID** (5 connections)
- **UUIDMappingXP** (5 connections) — `server/services/player_combat_service_support.py`
- **async_load_lifecycle_manager()** (4 connections) — `server/services/player_combat_service_support.py`
- **available_lifecycle_npc_ids()** (4 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (4 connections) — `server/services/player_combat_service_support.py`
- **Protocol** (4 connections)
- **.grant_xp()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_xp_value()** (3 connections) — `server/services/player_combat_service_support.py`
- **xp_int_from_base_stats_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **Player combat state, XP rewards, and NPC integration (UUID / lifecycle lookup…** (1 connections) — `server/services/player_combat_service.py`
- **Protocols and module-level helpers for player combat XP and lifecycle lookup.…** (1 connections) — `server/services/player_combat_service_support.py`
- **UUID mapping helper with XP lookup (NPCCombatUUIDMapping).** (1 connections) — `server/services/player_combat_service_support.py`
- **Return stored XP for npc_id when present.** (1 connections) — `server/services/player_combat_service_support.py`
- **Public read API from NPC combat integration.** (1 connections) — `server/services/player_combat_service_support.py`
- **Return UUID mapping helper.** (1 connections) — `server/services/player_combat_service_support.py`
- **XP/level authority surface used by player combat service (#879).** (1 connections) — `server/services/player_combat_service_support.py`
- **Award XP and level up (and run the level-up hook) if the curve says so.** (1 connections) — `server/services/player_combat_service_support.py`
- *... and 7 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [validate_secure_path](validate_secure_path.md) (3 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (1 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 70 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*