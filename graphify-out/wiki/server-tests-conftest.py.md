# server/tests/conftest.py

> 31 nodes · cohesion 0.14

## Key Concepts

- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **UUID** (10 connections)
- **player_preferences_service.py** (9 connections) — `server/services/player_preferences_service.py`
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
- **Player Preferences Service for Advanced Chat Channels. This module provides…** (1 connections) — `server/services/player_preferences_service.py`
- **Get preferences for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Update a player's default channel. Args: session: Database session player_id:…** (1 connections) — `server/services/player_preferences_service.py`
- **Mute a channel for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Unmute a channel for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Service for managing player channel preferences. This service handles: - Player…** (1 connections) — `server/services/player_preferences_service.py`
- **Get list of muted channels for a player. Args: session: Database session…** (1 connections) — `server/services/player_preferences_service.py`
- **Check if a specific channel is muted for a player. Args: session: Database…** (1 connections) — `server/services/player_preferences_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (3 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [MessageQueue](MessageQueue.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [compilerOptions](compilerOptions.md) (1 shared connections)

## Source Files

- `server/services/player_preferences_service.py`

## Audit Trail

- EXTRACTED: 75 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*