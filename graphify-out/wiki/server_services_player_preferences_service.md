# server services player preferences service

> 29 nodes

## Key Concepts

- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
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
- **Get preferences for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Update a player's default channel. Args: session: Database session player_id:…** (1 connections) — `server/services/player_preferences_service.py`
- **Mute a channel for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Unmute a channel for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- **Service for managing player channel preferences. This service handles: - Player…** (1 connections) — `server/services/player_preferences_service.py`
- **Get list of muted channels for a player. Args: session: Database session…** (1 connections) — `server/services/player_preferences_service.py`
- **Check if a specific channel is muted for a player. Args: session: Database…** (1 connections) — `server/services/player_preferences_service.py`
- **Initialize the PlayerPreferencesService. Note: This service now uses PostgreSQL…** (1 connections) — `server/services/player_preferences_service.py`
- **Delete preferences for a player. Args: session: Database session player_id: The…** (1 connections) — `server/services/player_preferences_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [server models player playerchannelpreferences](server_models_player_playerchannelpreferences.md) (4 shared connections)
- [server commands channel commands](server_commands_channel_commands.md) (2 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (2 shared connections)

## Source Files

- `server/services/player_preferences_service.py`

## Audit Trail

- EXTRACTED: 68 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*