# Dependency Upgrade Report

> 43 nodes

## Key Concepts

- **PlayerInventory** (25 connections) — `server/models/player.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Any** (5 connections)
- **Base** (4 connections)
- **InventoryPayload** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_coerce_row_stats()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_parse_equipped_safely()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_strings()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_numerics()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_player_inventory_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_with_data()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_multiple_rooms()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_table_name()** (2 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_table_name()** (2 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_table_name()** (2 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Player inventory model for persistent storage of items.      This matches the pl** (1 connections) — `server/models/player.py`
- **Junction table tracking which rooms each player has explored.** (1 connections) — `server/models/player.py`
- **Player** (1 connections)
- *... and 18 more nodes in this community*

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (19 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (6 shared connections)
- [Quality Audit Report](Quality_Audit_Report.md) (6 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (4 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (4 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (3 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 144 (86%)
- INFERRED: 24 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*