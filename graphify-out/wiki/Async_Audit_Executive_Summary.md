# Async Audit Executive Summary

> 32 nodes

## Key Concepts

- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerChannelPreferences** (15 connections) — `server/models/player.py`
- **test_player_channel_preferences_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_table_name()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_with_muted_channels()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_multiple_rooms()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_table_name()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_table_name()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_with_data()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Player channel preferences model for Advanced Chat Channels. Stores player…** (1 connections) — `server/models/player.py`
- **Unit tests for Player-related SQLAlchemy models. Tests…** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory has correct table name.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerInventory __repr__ method.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerExploration can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerExploration has correct table name.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerExploration __repr__ method.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerExploration can track multiple rooms for same player.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- *... and 7 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (15 shared connections)
- [logger.ts](logger.ts.md) (2 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [mark_player_seen_impl](mark_player_seen_impl.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 50 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*