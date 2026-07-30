# Test get room environment() treats

> 32 nodes

## Key Concepts

- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **test_player_channel_preferences_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_with_muted_channels()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
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
- **Junction table tracking which rooms each player has explored.** (1 connections) — `server/models/player.py`
- **Unit tests for Player-related SQLAlchemy models.  Tests PlayerChannelPreferences** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences has correct default values.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences can have muted channels.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences has correct table name.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences __repr__ method.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory has correct default values.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- *... and 7 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (10 shared connections)
- [test player preferences service](test_player_preferences_service.md) (5 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (3 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [metrics](metrics.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 82 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*