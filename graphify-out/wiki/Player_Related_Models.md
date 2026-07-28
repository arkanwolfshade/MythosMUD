# Player Related Models

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

- [Player Save Preparer](Player_Save_Preparer.md) (6 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (5 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (3 shared connections)
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Metadata Npc](Metadata_Npc.md) (1 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (1 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (1 shared connections)
- [Combat Attack Flow](Combat_Attack_Flow.md) (1 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (1 shared connections)

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