# Client ASCII Map API

> 31 nodes

## Key Concepts

- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **UUID** (10 connections)
- **player_preferences_service.py** (9 connections) — `server/services/player_preferences_service.py`
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
- **.__init__()** (2 connections) — `server/services/player_preferences_service.py`
- **._is_valid_json_array()** (2 connections) — `server/services/player_preferences_service.py`
- **Player Preferences Service for Advanced Chat Channels.  This module provides fun** (1 connections) — `server/services/player_preferences_service.py`
- **Service for managing player channel preferences.      This service handles:** (1 connections) — `server/services/player_preferences_service.py`
- **Initialize the PlayerPreferencesService.          Note: This service now uses Po** (1 connections) — `server/services/player_preferences_service.py`
- **Create default preferences for a new player.          Args:             session:** (1 connections) — `server/services/player_preferences_service.py`
- **Get preferences for a player.          Args:             session: Database sessi** (1 connections) — `server/services/player_preferences_service.py`
- **Update a player's default channel.          Args:             session: Database** (1 connections) — `server/services/player_preferences_service.py`
- **Mute a channel for a player.          Args:             session: Database sessio** (1 connections) — `server/services/player_preferences_service.py`
- **Unmute a channel for a player.          Args:             session: Database sess** (1 connections) — `server/services/player_preferences_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [Quality Audit Report](Quality_Audit_Report.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Async Persistence Delegates](Async_Persistence_Delegates.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)

## Source Files

- `server/services/player_preferences_service.py`

## Audit Trail

- EXTRACTED: 140 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*