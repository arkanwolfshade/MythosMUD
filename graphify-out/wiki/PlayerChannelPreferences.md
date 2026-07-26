# PlayerChannelPreferences

> 37 nodes · cohesion 0.12

## Key Concepts

- **PlayerChannelPreferences** (30 connections) — `server/models/player.py`
- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **UUID** (10 connections)
- **player_preferences_service.py** (9 connections) — `server/services/player_preferences_service.py`
- **.is_channel_muted()** (8 connections) — `server/services/player_preferences_service.py`
- **.mute_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.unmute_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.update_default_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **Any** (8 connections)
- **AsyncSession** (8 connections)
- **.create_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.delete_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.get_muted_channels()** (7 connections) — `server/services/player_preferences_service.py`
- **.get_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **._is_valid_channel()** (6 connections) — `server/services/player_preferences_service.py`
- **preferences_service()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **sample_preferences()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **.__init__()** (2 connections) — `server/services/player_preferences_service.py`
- **._is_valid_json_array()** (2 connections) — `server/services/player_preferences_service.py`
- **Player channel preferences model for Advanced Chat Channels.      Stores player** (1 connections) — `server/models/player.py`
- **Player Preferences Service for Advanced Chat Channels.  This module provides fun** (1 connections) — `server/services/player_preferences_service.py`
- **Get preferences for a player.          Args:             session: Database sessi** (1 connections) — `server/services/player_preferences_service.py`
- **Update a player's default channel.          Args:             session: Database** (1 connections) — `server/services/player_preferences_service.py`
- **Mute a channel for a player.          Args:             session: Database sessio** (1 connections) — `server/services/player_preferences_service.py`
- *... and 12 more nodes in this community*

## Relationships

- [PlayerInventory](PlayerInventory.md) (6 shared connections)
- [test_player_preferences_service.py](test_player_preferences_service.py.md) (5 shared connections)
- [Player](Player.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_lucidity_models.py](test_lucidity_models.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Base](Base.md) (1 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)
- [PlayerEffect](PlayerEffect.md) (1 shared connections)
- [__init__.py](__init__.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 158 (84%)
- INFERRED: 30 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*