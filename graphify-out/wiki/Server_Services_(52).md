# Server Services (52)

> 35 nodes

## Key Concepts

- **PlayerChannelPreferences** (30 connections) — `server/models/player.py`
- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **UUID** (10 connections)
- **AsyncSession** (8 connections)
- **Any** (8 connections)
- **.update_default_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.mute_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.unmute_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.is_channel_muted()** (8 connections) — `server/services/player_preferences_service.py`
- **.create_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.get_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.get_muted_channels()** (7 connections) — `server/services/player_preferences_service.py`
- **.delete_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **._is_valid_channel()** (6 connections) — `server/services/player_preferences_service.py`
- **preferences_service()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **sample_preferences()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **.__init__()** (2 connections) — `server/services/player_preferences_service.py`
- **._is_valid_json_array()** (2 connections) — `server/services/player_preferences_service.py`
- **Player channel preferences model for Advanced Chat Channels.      Stores player** (1 connections) — `server/models/player.py`
- **Service for managing player channel preferences.      This service handles:** (1 connections) — `server/services/player_preferences_service.py`
- **Initialize the PlayerPreferencesService.          Note: This service now uses Po** (1 connections) — `server/services/player_preferences_service.py`
- **Create default preferences for a new player.          Args:             session:** (1 connections) — `server/services/player_preferences_service.py`
- **Get preferences for a player.          Args:             session: Database sessi** (1 connections) — `server/services/player_preferences_service.py`
- **Update a player's default channel.          Args:             session: Database** (1 connections) — `server/services/player_preferences_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [Server Services](Server_Services.md) (7 shared connections)
- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Models (21)](Server_Models_%2821%29.md) (5 shared connections)
- [Server Services (16)](Server_Services_%2816%29.md) (4 shared connections)
- [Server Models (17)](Server_Models_%2817%29.md) (2 shared connections)
- [Server Persistence (11)](Server_Persistence_%2811%29.md) (1 shared connections)
- [Server Models (26)](Server_Models_%2826%29.md) (1 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 148 (83%)
- INFERRED: 30 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*