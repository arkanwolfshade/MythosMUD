# commands inventory helpers

> 29 nodes

## Key Concepts

- **PlayerInventory** (25 connections) — `server/models/player.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **Base** (4 connections)
- **InventoryPayload** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
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
- **Type hint for inventory payload structure.** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Unit tests for Player-related SQLAlchemy models.  Tests PlayerChannelPreferences** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences has correct table name.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory has correct default values.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory can have inventory and equipped data.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory has correct table name.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory __repr__ method.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- *... and 4 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (7 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (6 shared connections)
- [combat models rationale](combat_models_rationale.md) (5 shared connections)
- [npc population stats](npc_population_stats.md) (3 shared connections)
- [task registry app](task_registry_app.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [command factories communication](command_factories_communication.md) (2 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 87 (78%)
- INFERRED: 24 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*