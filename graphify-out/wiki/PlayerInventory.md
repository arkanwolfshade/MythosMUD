# PlayerInventory

> 60 nodes

## Key Concepts

- **PlayerInventory** (19 connections) — `server/models/player.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerChannelPreferences** (16 connections) — `server/models/player.py`
- **test_procedures_return_shape.py** (13 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **PlayerExploration** (11 connections) — `server/models/player.py`
- **test_clear_player_inventory_empties_gear_and_leaves_stats_untouched()** (9 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_add_player_effect_generates_id()** (8 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_player_server_defaults.py** (7 connections) — `server/tests/unit/models/test_player_server_defaults.py`
- **test_get_npc_system_statistics_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **async_sessionmaker** (6 connections)
- **asyncio** (6 connections)
- **AsyncSession** (6 connections)
- **test_server_default_renders_the_same_ddl()** (4 connections) — `server/tests/unit/models/test_player_server_defaults.py`
- **Base** (4 connections)
- **test_player_channel_preferences_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_table_name()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_with_muted_channels()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_multiple_rooms()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- *... and 35 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [session_factory](session_factory.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [PlayerPreferencesService](PlayerPreferencesService.md) (2 shared connections)
- [session](session.md) (2 shared connections)
- [test_player_preferences_service.py](test_player_preferences_service.py.md) (1 shared connections)
- [preferences_service](preferences_service.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/models/test_player_related_models.py`
- `server/tests/unit/models/test_player_server_defaults.py`

## Audit Trail

- EXTRACTED: 111 (85%)
- INFERRED: 20 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*