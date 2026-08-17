# server services npc combat data

> 31 nodes

## Key Concepts

- **NPCCombatDataProvider** (30 connections) — `server/services/npc_combat_data_provider.py`
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

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (7 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (5 shared connections)
- [server services combat initialization](server_services_combat_initialization.md) (4 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 54 (79%)
- INFERRED: 14 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*