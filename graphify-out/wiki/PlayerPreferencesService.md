# PlayerPreferencesService

> 33 nodes

## Key Concepts

- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **PlayerChannelPreferences** (15 connections) — `server/models/player.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **player_preferences_service.py** (10 connections) — `server/services/player_preferences_service.py`
- **UUID** (10 connections)
- **Any** (8 connections)
- **AsyncSession** (8 connections)
- **.create_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.is_channel_muted()** (7 connections) — `server/services/player_preferences_service.py`
- **.mute_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **.unmute_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **.update_default_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **.delete_player_preferences()** (6 connections) — `server/services/player_preferences_service.py`
- **.get_muted_channels()** (6 connections) — `server/services/player_preferences_service.py`
- **.get_player_preferences()** (6 connections) — `server/services/player_preferences_service.py`
- **._is_valid_channel()** (6 connections) — `server/services/player_preferences_service.py`
- **.__init__()** (2 connections) — `server/services/player_preferences_service.py`
- **._is_valid_json_array()** (2 connections) — `server/services/player_preferences_service.py`
- **Player channel preferences model for Advanced Chat Channels. Stores player…** (1 connections) — `server/models/player.py`
- **Player Preferences Service for Advanced Chat Channels. This module provides…** (1 connections) — `server/services/player_preferences_service.py`
- **Get preferences for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Update a player's default channel. Args: session: Database session player_id:…** (1 connections) — `server/services/player_preferences_service.py`
- **Mute a channel for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Unmute a channel for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Service for managing player channel preferences. This service handles: - Player…** (1 connections) — `server/services/player_preferences_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [Player](Player.md) (11 shared connections)
- [test_player_preferences_service.py](test_player_preferences_service.py.md) (3 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (3 shared connections)
- [preferences_service](preferences_service.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/player_preferences_service.py`

## Audit Trail

- EXTRACTED: 81 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*